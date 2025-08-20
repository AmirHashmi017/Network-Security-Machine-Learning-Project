from networksecurity.exception.exception import NetworkSecuityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.entity.artifact_entity import DataValidationArtifact
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file,write_yaml_file

import os
import sys
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact= data_ingestion_artifact
            self.data_validation_config= data_validation_config
            self.schema_config= read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecuityException(e,sys)
    
    @staticmethod
    def read_data(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise NetworkSecuityException(e,sys)
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns=len(self.schema_config["columns"])
            logging.info(f"Required Number of columns are: {number_of_columns}")
            dataFrame_columns= len(dataframe.columns)
            logging.info(f"Number of columns in dataset are: {dataFrame_columns}")
            if number_of_columns==dataFrame_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecuityException(e,sys)
    
    def validate_numeric_columns(self,dataFrame:pd.DataFrame)->bool:
        try:
            numeric_columns=[column for column in dataFrame.columns 
                             if pd.api.types.is_numeric_dtype(dataFrame[column])]
            if len(numeric_columns)>0:
                return True
            return False
        except Exception as e:
            raise NetworkSecuityException(e,sys)
    
    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_same_dist=ks_2samp(d1,d2)
                if threshold<=is_same_dist.pvalue:
                    isFound=False
                else:
                    isFound=True
                    status=False
                report.update({column:{
                    "p_value":float(is_same_dist.pvalue),
                    "drift_status":isFound
                }})
            
            drift_report_file_path= self.data_validation_config.drift_report_file_path
            dir_path=os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(drift_report_file_path,report)
            return status

        except Exception as e:
            raise NetworkSecuityException(e,sys)
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            error_message=""
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            train_dataframe= DataValidation.read_data(train_file_path)
            test_dataframe= DataValidation.read_data(test_file_path)

            status= self.validate_number_of_columns(train_dataframe)
            if not status:
                error_message="Columns are missing in training dataframe"
            status= self.validate_number_of_columns(test_dataframe)
            if not status:
                error_message="Columns are missing in test dataframe"
            status= self.validate_numeric_columns(train_dataframe)
            if not status:
                error_message="Numeric Columns are missing in training dataframe"
            status= self.validate_numeric_columns(test_dataframe)
            if not status:
                error_message="Numeric Columns are missing in test dataframe"
            
            # let's check data drift
            status= self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)
            if not status:
                error_message= "There is Data Drift in dataset"
            if error_message!="":
                dir_path= os.path.dirname(self.data_validation_config.invalid_train_file_path)
                os.makedirs(dir_path,exist_ok=True)
                train_dataframe.to_csv(self.data_validation_config.invalid_train_file_path,index=False
                                       ,header=True)
                test_dataframe.to_csv(self.data_validation_config.invalid_test_file_path,index=False
                                   ,header=True)
                data_validation_artifact= DataValidationArtifact(
                    validation_status=False,
                    valid_train_file_path=None,
                    valid_test_file_path= None,
                    invalid_train_file_path= self.data_validation_config.invalid_train_file_path ,
                    invalid_test_file_path= self.data_validation_config.invalid_test_file_path,
                    drift_report_file_path= self.data_validation_config.drift_report_file_path
                )
            else:
                dir_path= os.path.dirname(self.data_validation_config.valid_train_file_path)
                os.makedirs(dir_path,exist_ok=True)
                train_dataframe.to_csv(self.data_validation_config.valid_train_file_path,index=False
                                       ,header=True)
                test_dataframe.to_csv(self.data_validation_config.valid_test_file_path,index=False
                                   ,header=True)
                data_validation_artifact= DataValidationArtifact(
                    validation_status=True,
                    valid_train_file_path=self.data_validation_config.valid_train_file_path,
                    valid_test_file_path= self.data_validation_config.valid_test_file_path,
                    invalid_train_file_path= None,
                    invalid_test_file_path= None,
                    drift_report_file_path= self.data_validation_config.drift_report_file_path
                )
            return data_validation_artifact
        
        except Exception as e:
            raise NetworkSecuityException(e,sys)
