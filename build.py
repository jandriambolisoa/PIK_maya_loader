import os
import os.path
import platform
import shutil
import sys

MODULE_FILENAME = "PIK_maya_loader.mod"

def build(source_path, build_path, install_path, targets):

    def get_module_infos():
        """Get module infos

        Returns:
            dict: infos about module
        """
        infos = {}
        
        platforms = {"Windows": "win", "Linux": "linux"}
        os_platform = platform.system()
        os_platform = platforms.get(os_platform, "mac")

        architectures = {"AMD64": "64"}
        os_architecture = platform.machine()
        os_architecture = architectures.get(os_architecture, "")
        
        infos["maya_version"] = os.environ.get("REZ_MAYA_VERSION").split(".")[0]
        infos["platform"] = f"{os_platform}{os_architecture}"
        infos["module_name"] = os.environ.get("REZ_BUILD_PROJECT_NAME")
        infos["module_version"] = os.environ.get("REZ_BUILD_PROJECT_VERSION")

        return infos

    def write_module_file():
        
        infos = get_module_infos()

        instructions = [
            "+",
            "MAYAVERSION:%s" %(infos.get("maya_version", "2025")),
            "PLATFORM:%s" %(infos.get("platform", "win64")),
            "%s" %(infos.get("module_name")),
            "%s" %(infos.get("module_version")),
            "../",
        ]
        content = " ".join(instructions)

        directory = os.path.join(
            build_path,
            "python",
            "PIK_maya_loader",
            "module",
        )

        os.makedirs(directory)
        with open(os.path.join(directory, MODULE_FILENAME), "x") as file:
            file.write(content)


    def _build():

        # python source
        src_py = os.path.join(source_path, "python")
        dest_py = os.path.join(build_path, "python")

        if not os.path.exists(dest_py):
            shutil.copytree(src_py, dest_py)

        write_module_file()

    def _install():
        src = os.path.join(build_path, "python")
        dest = os.path.join(install_path, "python")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:]
    )
