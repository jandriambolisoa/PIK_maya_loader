import os

from maya import cmds
from maya import OpenMaya


def get_available_plugins():
    """List loadable plugins and their paths

    Returns:
        dict: The plugin name and its path
    """

    plugins_paths = os.getenv("MAYA_PLUG_IN_PATH").split(";")
    plugins = {}

    for path in plugins_paths:
        try:
            files = os.listdir(path)
            for f in files:
                # Add plugin name as key and plugin path as value in 'plugins' dictionnary
                plugins[os.path.splitext(f)[0]] = os.path.join(path, f).replace(
                    "\\", "/"
                )
        except RuntimeError:
            pass

    return plugins


def load_and_set_autoload_for_plugin(pluginPath: str):
    """Check if a plugin is loaded. If not, load and set autoload
    to True.

    Args:
        pluginPath (str): Filepath to a maya plugin
    """
    try:
        loaded, autoload, _ = cmds.pluginInfo(pluginPath, query=True, settings=True)

        if not loaded:
            cmds.loadPlugin(pluginPath, quiet=True)
        if not autoload:
            cmds.pluginInfo(pluginPath, edit=True, autoload=True)
    except RuntimeError:
        OpenMaya.MGlobal.displayError(
            "# PIK_maya_loader - a plugin failed to load : %s" % pluginPath
        )
