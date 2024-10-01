''' 
We are making our package that we can install using pip install .  pip install -r requirements.txt
'''

from setuptools import find_packages,setup
from typing import List
def get_requirements(filename:str)->List[str]:
    ''' 
    This function reads the requirements.txt file and returns the list of requirements
    '''
    Hypen_e_dot='-e .'
    requirements = []
    with open(filename, 'r') as file:
        requirements = file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author='Sushant',
    author_email='sushantniraula01@gmail.com',
    packages=find_packages(),# searches for __init__.py file in the directory and includes the directory as a package
    install_requires=get_requirements('requirements.txt')
)