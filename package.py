name = "PIK_maya_loader"

version = "0.1.4"

authors = [
    "Jeremy Andriambolisoa",
]

description = \
    """
    Load menu and plugins in maya at startup.
    """

requires = [
    "python-3+",
    "maya-2025"
]

uuid = "piktura.PIK_maya_loader"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.MAYA_MODULE_PATH.append("{root}/python/PIK_maya_loader/module")