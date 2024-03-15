import subprocess
import pkg_resources
from pkg_resources import parse_requirements, DistributionNotFound

# 读取requirements.txt文件中的所有库
with open('requirements.txt') as f:
    requirements = parse_requirements(f.read())

# 安装缺失的库，或者安装新版本的库
for requirement in requirements:
    try:
        module_name = requirement.name
        if requirement.specifier:
            required_version = str(requirement.specifier)
            installed_version = pkg_resources.get_distribution(module_name).version
            if installed_version not in required_version:
                subprocess.check_call(['pip', 'install', f"{module_name}{required_version}"])
        else:
            __import__(module_name)
    except (DistributionNotFound, pkg_resources.VersionConflict, ModuleNotFoundError):
        subprocess.check_call(['pip', 'install', str(requirement)])
from sanic_app import main

if __name__ == "__main__":
    main()