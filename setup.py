'''
The setup.py is an essential part of packaging and distributing python projects. It is used by
setup tools to define the configuration of your project, such as, it's metadata, dependencies and
more.
'''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirments
    '''
    requirement_list=[]
    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt cannot find")

    return requirement_list

setup(
name="Network Security",
version="0.0.1",
author="Amir Hashmi",
author_email="amirhashmi017@gmail.com",
packages=find_packages(),
install_requires=get_requirements()
)
