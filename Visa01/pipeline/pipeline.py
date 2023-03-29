import sys
from Visa01.components.data_ingestion import DataIngestion
from Visa01.configuration.configuration import Configuration
from Visa01.entity.entity_artifact import DataIngestionArtifact
from Visa01.exception import CustomException
from Visa01.logger import logging

class Pipeline() :
    def __init__(self, configuration: Configuration = Configuration()) -> None:
        
        try :
            self.confugiration = configuration

        except Exception as e :
            raise CustomException(e, sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact :
        
        try :
            data_ingestion = DataIngestion(data_ingestion_config = self.confugiration.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        
        except Exception as e :
            raise CustomException(e,sys) from e
        
    def run_pipeline(self) :
        
        try :
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e :
            raise CustomException(e,sys) from e