import os

from maya import cmds
from maya import OpenMaya

try:
    import tweener

    plugin_folderpath, _ = os.path.split(tweener.__file__)
    plugin_filepath = os.path.join(plugin_folderpath, "tweener.py")

    # Manually load plugin if not loaded yet
    if not cmds.pluginInfo(plugin_filepath, q=True, loaded=True):
        cmds.loadPlugin(plugin_filepath)
    cmds.tweener()

except Exception as e:
    OpenMaya.MGlobal.displayError(e)
