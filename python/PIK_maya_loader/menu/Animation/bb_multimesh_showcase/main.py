from maya import OpenMaya

try:
    from bb_multimesh_showcase import main as bb_multimesh_showcase

    exec(open(bb_multimesh_showcase.__file__).read())
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
