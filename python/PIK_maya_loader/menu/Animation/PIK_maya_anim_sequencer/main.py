from maya import OpenMaya

try:
    from PIK_maya_anim_sequencer.scripts.main import run

    run()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
