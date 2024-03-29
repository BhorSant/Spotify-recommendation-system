import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from music_recommend.logger.log import logging
from music_recommend.config.configuration import AppConfiguration
from music_recommend.exception.exception_handler import AppException

class ModelTrainer:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e,sys) from e
        
    def train(self):
        try:
            # loading pivot table
            music_pivot = pickle.load(self.model_trainer_config.transformed_data_file_dir,"rb")
            music_sparse = csr_matrix(music_pivot)
            # Training model
            model = NearestNeighbors(metric="cosine", algorithm="brute")
            model.fit(music_sparse)

            # saving model object for recommendations
            os.makedirs(self.model_trainer_cofig.trainer_model_dir,exist_ok=True)
            file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(model,open(file_name,"wb"))
            logging.info(f"Trained model saved in {file_name}")

        except Exception as e:
            raise AppException(e,sys) from e
    
    def initialize_model_trainer(self):
        try:
            logging.info(f"{'=*20'} Model Trainer log Started.{'=*20'}")
            self.train()
            logging.info(f"{'=*20'} Model Trainer log Ended.{'=*20'}")
        except Exception as e:
            raise AppException(e,sys) from e