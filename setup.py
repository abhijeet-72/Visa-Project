from setuptools import setup, find_packages
from typing import List

requirements_file = 'requirements.txt'
HYPHEN_E_DOT = '-e .'

def get_requirements() -> List[str] :
    with open(requirements_file) as file :
        requirements = file.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]

        if HYPHEN_E_DOT in requirements :
            requirements.remove(HYPHEN_E_DOT)
        
        return requirements

setup(
    name = 'Machine Learning Project',
    version = '0.0.1',
    description = 'US Visa approval prediction project',
    author = 'Abhijit',
    author_email = 'aj.datsc72@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
    )