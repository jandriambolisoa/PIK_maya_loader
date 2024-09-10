import maya.OpenMaya as om

try:
    import studiolibrary

    studiolibrary.main()
except Exception as e:
    om.MGlobal.displayError(e)
