from maya import OpenMaya

try:
    from tx_stickyController import install

    install.install()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
