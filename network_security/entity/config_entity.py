from datetime import datetime
import os 
from network_security.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        """
        Constructor for TrainingPipelineConfig class

        timestamp: The timestamp value to be used for directory naming
        """
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.PIPELINE_NAME=training_pipeline.PIPELINE_NAME
        self.ARTIFACT_NAME=training_pipeline.ARTIFACT_DIR
        self.ARTIFACT_DIR=os.path.join(self.ARTIFACT_NAME,timestamp)
        self.TIMESTAMP=timestamp
        
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        """
        Data Ingestion related configuration

        params:
        training_pipeline_config: The instance of TrainingPipelineConfig

        """

        self.data_ingestion_dir:str=os.path.join(training_pipeline_config.ARTIFACT_DIR,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME)
        self.training_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
        self.testing_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)       
        self.train_test_split_ratio=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str = training_pipeline.DATA_INGESTION_DATABASE_NAME