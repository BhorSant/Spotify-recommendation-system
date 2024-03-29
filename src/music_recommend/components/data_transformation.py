import os
import sys
import pickle
import pandas as pd
from music_recommend.logger.log import logging
from music_recommend.config.configuration import AppConfiguration
from music_recommend.exception.exception_handler import AppException

class DataTransformation:
    def __init__(self,app_config = AppConfiguration()):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()

        except Exception as e:
            raise AppException(e,sys) from e
        
    def get_data_transformer(self):
        try:
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)
            music_pivot = df.pivot_table(index="name", columns="artists", values="popularity", aggfunc="sum")
            logging.info(f"Shape of music pivot table : {music_pivot.shape}")
            music_pivot.fillna(0,inplace=True)

            # Saving pivot table data
            os.makedirs(self.data_transformation_config.transformed_data_dir,exist_ok=True)
            pickle.dump(music_pivot,open(os.path.join(self.data_transformation_config.transformed_data_dir, "transformed_data.pkl"),'wb'))
            logging.info(f"Transformed data saved in {self.data_transformation_config.transformed_data_dir}")
        
            #  keeping music names 
            music_names = music_pivot.index

            # Saving music_names objects for web app
            os.makedirs(self.data_validation_config.validated_data_dir,exist_ok=True)
            pickle.dump(music_names,open(os.path.join(self.data_validation_config.validated_data_dir, "music_name.pkl"),'wb'))
            logging.info(f"Transformed data names saved in {self.data_validation_config.validated_data_dir}")

            # Saving music_pivot objects for web
            os.makedirs(self.data_validation_config.serialized_object_dir,exist_ok=True)
            pickle.dump(music_pivot,open(os.path.join(self.data_validation_config.serialized_object_dir, "music_pivot.pkl"),'wb'))
            logging.info(f'Saved music_pivot serialized object to {self.data_validation_config.serialized_object_dir}')

        except Exception as e:
            raise AppException(e, sys) from e

    

    def initiate_data_transformation(self):
        try:
            logging.info(f"{'='*20}Data Transformation log started.{'='*20} ")
            self.get_data_transformer()
            logging.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e