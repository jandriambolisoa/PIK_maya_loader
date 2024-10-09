import maya.OpenMaya as om

try:
    from aTools import setup

    setup.install()
except Exception as e:
    om.MGlobal.displayError(e)
