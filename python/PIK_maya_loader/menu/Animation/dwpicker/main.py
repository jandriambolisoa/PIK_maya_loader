from maya import OpenMaya

try:
    import dwpicker
    
    dwpicker.show()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
