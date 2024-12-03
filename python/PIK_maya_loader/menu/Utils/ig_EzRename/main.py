import maya.OpenMaya as om

try:
    import ig_EzRename
    ig_EzRename.UI()
except Exception as e:
    om.MGlobal.displayError(e)
