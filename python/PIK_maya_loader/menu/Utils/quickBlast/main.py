import maya.OpenMaya as om

try:
    from quickBlast.main import run
    
    run()
except Exception as e:
    om.MGlobal.displayError(e)
