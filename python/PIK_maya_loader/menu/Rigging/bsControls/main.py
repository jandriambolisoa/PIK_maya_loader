import maya.OpenMaya as om

try:
    from bsControls import bs_controlsUI

    bsCon = bs_controlsUI.BSControlsUI()
    bsCon.bsControlsUI()
except Exception as e:
    om.MGlobal.displayError(e)
