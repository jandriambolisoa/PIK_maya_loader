import maya.OpenMaya as om

try:
    import ngSkinTools2

    ngSkinTools2.open_ui()
except Exception as e:
    om.MGlobal.displayError(e)
