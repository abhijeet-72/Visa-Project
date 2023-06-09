import os
from datetime import datetime

def get_current_timestamp() :
    return f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'

CURRENT_TIMESTAMP = get_current_timestamp()

ROOT_DIR = os.getcwd()
CONFIG_DIR = 'config'
CONFIG_FILE = 'config.yaml'

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE)

DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_DOWNLOAD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_INGESTED_DIR_KEY = 'ingested_data_dir'
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = 'ingested_train_dir' 
DATA_INGESTION_INGESTED_TEST_DIR_KEY = 'ingested_test_dir' 

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
PIPELINE_NAME_KEY = 'pipeline_name'
PIPELINE_ARTIFACT_DIR_KEY = 'pipeline_artifact_dir'

COLUMN_COMPANY_AGE = 'company_age'
COLUMN_YEAR_ESTB = 'yr_of_estab'
COLUMN_ID = 'case_id'
COLUMN_CASE_STATUS = 'case_status'
