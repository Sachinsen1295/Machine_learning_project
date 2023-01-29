import yaml
from housing.exception import HousingException
import os,sys

"""
We use util file to use helper function
"""


def read_yaml_file(file_path:str) ->dict:

    """
    To read yaml file and return the content as dictinary
    file_path : str
    """

    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e

