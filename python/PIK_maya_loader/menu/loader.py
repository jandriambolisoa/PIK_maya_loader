import os
import json

from maya import cmds
from maya import mel
from maya import OpenMaya


class MenuLoader:
    def __init__(self, menu_name):
        """Init the menu

        Args:
            menu_name (str): The name of the menu
        """
        self.menu_name = menu_name
        self.gMainWindow = mel.eval("$tmpVar = $gMainWindow")

    def create_menu(self):
        """Create the main menu"""
        OpenMaya.MGlobal.displayInfo("# PIK_maya_loader - loading menu")

        # Check if the menu exists, delete if it does
        if cmds.menu(self.menu_name, exists=True):
            cmds.deleteUI(self.menu_name)

        # Create the menu
        menu = cmds.menu(self.menu_name, parent=self.gMainWindow)
        cmds.menuItem(divider=True, dividerLabel="PIKTURA - tools", parent=menu)

        self.create_submenus_with_scripts(menu)

    def create_submenus_with_scripts(self, parent):
        """Create a deployable menu for each sub menu

        Args:
            parent (string): path to a maya menu
        """

        # Get sub menus
        folder_path, _ = os.path.split(os.path.normpath(__file__))
        submenus = [
            folder
            for folder in os.listdir(folder_path)
            if os.path.isdir(os.path.join(folder_path, folder))
            and "__pycache__" not in folder
        ]

        for submenu in submenus:
            # Create sub menus
            submenu_item = cmds.menuItem(
                submenu, label=submenu, subMenu=True, parent=parent
            )
            submenu_scripts = os.listdir(os.path.join(folder_path, submenu))

            for script in submenu_scripts:
                # Get script datas and main file
                script_folder = os.path.join(folder_path, submenu, script)
                datas = os.path.join(script_folder, "datas.json")

                if not os.path.isfile(datas):
                    continue
                with open(datas, "r") as jsonFile:
                    script_datas = json.load(jsonFile)

                # Get script infos
                script_filename = next(
                    iter([f for f in os.listdir(script_folder) if "main" in f])
                )
                _, script_filetype = os.path.splitext(script_filename)

                script_type = {".py": "python", ".mel": "mel"}

                # Get script content
                with open(
                    os.path.join(folder_path, submenu, script, "main.py"), "r"
                ) as s:
                    script_content = s.read()

                # Check if script works
                try:
                    exec("import %s" % script)
                except ModuleNotFoundError:
                    continue

                OpenMaya.MGlobal.displayInfo("# PIK_maya_loader - loaded %s" % script)
                # Create menu item
                cmds.menuItem(
                    script_datas["label"],
                    annotation=script_datas["annotation"],
                    image="%s.png" % script,
                    command=script_content,
                    sourceType=script_type[script_filetype],
                    parent=submenu_item,
                )
