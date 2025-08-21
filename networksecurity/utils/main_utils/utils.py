import yaml
from networksecurity.exception.exception import NetworkSecuityException
from networksecurity.logging.logger import logging
import os,sys
import pickle
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

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

def load_numpy_array_data(filepath):
    try:
        with open(filepath,'rb') as file_obj:
            return np.load(file_obj)
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

def load_object(filepath):
    try:
        with open(filepath,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkSecuityException(e,sys)
    
def evaluate_models(X_train,Y_train,X_test,Y_test,models,params)->dict:
    report={}
    for i in range (len(list(models))):
        model= list(models.values())[i]
        para= params[list(models.keys())[i]]

        gs= GridSearchCV(estimator=model,param_grid=para,cv=3)
        gs.fit(X_train,Y_train)

        model.set_params(**gs.best_params_)
        model.fit(X_train,Y_train)

        Y_train_pred= model.predict(X_train)
        Y_test_pred= model.predict(X_test)

        train_model_score= r2_score(Y_train,Y_train_pred)
        test_model_score= r2_score(Y_test,Y_test_pred)

        report[list(models.keys())[i]]=test_model_score
    
    return report



