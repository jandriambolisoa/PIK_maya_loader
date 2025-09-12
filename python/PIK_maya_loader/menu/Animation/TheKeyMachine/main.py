from maya import OpenMaya

try:
    import TheKeyMachine
    
    TheKeyMachine.toggle()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
