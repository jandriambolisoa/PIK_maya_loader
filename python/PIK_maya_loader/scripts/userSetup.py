from maya import cmds

from PIK_maya_loader.menu import loader
from PIK_maya_loader.plugins import utils


def main():
    """Execute actions to setup Maya."""

    # Load menu
    menu_loader = loader.MenuLoader("PIK")
    menu_loader.create_menu()

    # Load plugins
    PLUGINS_TO_LOAD = ["AbcImport", "AbcExport"]
    all_plugins = utils.get_available_plugins()
    for plugin in PLUGINS_TO_LOAD:
        utils.load_and_set_autoload_for_plugin(all_plugins[plugin])


# Execute the main function after the loading of the ui.
cmds.evalDeferred(main, lp=True)
