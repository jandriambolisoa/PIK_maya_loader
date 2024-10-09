from maya import OpenMaya

try:
    from js_stickyMod import ui

    ui.ui()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
