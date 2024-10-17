from maya import OpenMaya

try:
    from animBot._api.core import CORE as ANIMBOT_CORE

    ANIMBOT_CORE.trigger.animBotMenu_toggle()
except Exception as e:
    OpenMaya.MGlobal.displayError(e)
