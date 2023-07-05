from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        "When the cursor goes to next line there will be \n added so we are replacing \n with blank"

        ''' -e . should not come while reading requirements.txt so: '''
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
setup(
name = 'mlproject',
version='0.0.1',
author='Pratiksha',
author_email='pmmanjrekar102@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)