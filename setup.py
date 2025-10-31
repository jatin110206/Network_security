'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''


from setuptools import find_packages,setup
from typing import List
import sys


def get_requirments()->List[str]:
    """
    this function will return list of requirments
    """
    requirments_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # we will read lines
            lines=file.readlines()
            # process each line
            for line in lines:
                requirments=line.strip()
                ## ignore the empty line and -e. lines
                if requirments and requirments!='-e .':
                    requirments_lst.append(requirments)
                

            
    except FileNotFoundError:
        print("requirments.txt not found") 
        
        
    return requirments_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Jatin Prakash Rathore",
    author_email="jatinprakashrathore@gmail.com",
    packages=find_packages(),
    install_requiers=get_requirments(),
)