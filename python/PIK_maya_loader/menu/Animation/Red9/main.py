from maya import OpenMaya

try:
    import Red9

    Red9.start()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
