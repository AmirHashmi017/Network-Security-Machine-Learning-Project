import yaml
from networksecurity.exception.exception import NetworkSecuityException
from networksecurity.logging.logger import logging
import os,sys
import pickle
import numpy as np

def read_yaml_file(file_path: str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise NetworkSecuityException(e,sys)

def write_yaml_file(filepath:str,content:object,replace:bool= False)->None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,'w') as file:
            yaml.dump(content,file)
    except Exception as e:
        raise NetworkSecuityException(e,sys)

def save_numpy_array_data(filepath,array:np.array):
    try:
        dir_path=os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath,'wb') as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise NetworkSecuityException(e,sys)
    
def save_object(filepath,obj):
    try:
        dir_path=os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise NetworkSecuityException(e,sys)
