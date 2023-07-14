from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
       requirements = file_obj.read().splitlines()
       requirements = [req.strip() for req in requirements if req.strip() != "-e ."]
    return requirements    

setup(
name ='ml-project',
version='0.0.1',
author ='kaushik',
author_email='srinukaus@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)