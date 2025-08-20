import os
import sys
import numpy as np
import pandas as pd

'''
Defining common constant variables for training pipeline
'''
TARGET_COLUMN="Result"
PIPELINE_NAME= "NetworkSecurity"
ARTIFACT_DIR= "Artifacts"
FILENAME= "phisingData.csv"

TRAIN_FILE_NAME= "train.csv"
TEST_FILE_NAME= "test.csv"

SCHEMA_FILE_PATH= os.path.join("data_schema","schema.yaml")

'''
Data Ingestion related constants.
'''
DATA_INGESTION_COLLECTION_NAME= "NetworkData"
DATA_INGESTION_DATABASE_NAME= "NetworkSecurityML"
DATA_INGESTION_DIR_NAME= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR= "feature_store"
DATA_INGESTION_INGESTED_DIR= "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO= 0.2

'''
Data Validation Constants
'''
DATA_VALIDATION_DIR_NAME= "data_validation"
DATA_VALIDATION_VALID_DIR= "validated"
DATA_VALIDATION_INVALID_DIR= "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR= "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME= "report.yaml"

'''
Data Transformation Constants
'''
DATA_TRANSFORMATION_DIR_NAME= "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"
DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"