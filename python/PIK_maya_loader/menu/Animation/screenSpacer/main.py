from maya import OpenMaya

try:
    from screenSpacer import screenspacer_Script
    OpenMaya.MGlobal.displayInfo("Screen Spacer UI loaded")

except Exception as e:
    OpenMaya.MGlobal.displayError(e)
