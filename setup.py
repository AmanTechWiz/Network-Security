from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]

    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("File not found!")

    return requirement_lst

setup(
    name="Network Security ML project",
    version="0.1",
    author="Amandeep",
    author_email="amantechwiz@example.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
