from setuptools import setup,find_packages
from typing import List

# Declaring variables for setup function

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR_NAME = "SACHIN SEN"
DESCRIPTION = "Machine Learning project"
# PACKAGES=["housing"]     #list of folder,  we can use find packages
REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirements_list() ->List[str]:
    
    """
    Description: This function is going to return list of requirement
    mentioned in reuquirements.txt file
    
    returns: This function is goinf to return the list which contain name of 
    libraries mentioned in requirement.txt file 
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


#Declaring variables for setup functions




setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    description=DESCRIPTION,
    packages=find_packages(),  
    install_requires=get_requirements_list()
      
    
)


"""also ind_packages() can be used insted of PACKAGES directly,
    it will return all the folder name where init is there"""
    
""" '-e .' is used to install package like in this housing folder we have"""

