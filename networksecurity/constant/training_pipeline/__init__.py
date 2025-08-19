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

'''
Data Ingestion related constants.
'''
DATA_INGESTION_COLLECTION_NAME= "NetworkData"
DATA_INGESTION_DATABASE_NAME= "NetworkSecurityML"
DATA_INGESTION_DIR_NAME= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR= "feature_store"
DATA_INGESTION_INGESTED_DIR= "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO= 0.2