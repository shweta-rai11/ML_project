



from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Read and process the requirements file.
    Returns a list of dependencies.
    """
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sweta',
    author_email='raiishweta808@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
