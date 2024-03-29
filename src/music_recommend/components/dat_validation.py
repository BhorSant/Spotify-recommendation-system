import os
import sys
import ast
import pandas as pd
import pickle
from music_recommend.exception.exception_handler import AppException
from music_recommend.logger.log import logging
from music_recommend.config.configuration import AppConfiguration

class DataValidation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.data_validation_config= app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e
        
    def preprocess_data(self):
        try:
            spotify = pd.read_csv(self.data_validation_config.music_csv_file)

            logging.info(f"Shape of Spotify Dataset : {spotify.shape}")
            logging.info(f"Columns of Spotify Dataset : {spotify.columns}")

            spotify = spotify['artists', 'name', 'popularity', 'release_date']

            # Let's store the data in the song have more the 30 popularity is given in new dataset
            df_popular = spotify[spotify["popularity"] > 31]
            x = df_popular["artists"].value_counts() > 2
            y = x[x].index
            df_popular = df_popular[df_popular["artists"].isin(y)]
            # let's drop the duplicates
            df_popular = df_popular.drop_duplicates(["name"])
            logging.info(f"Shape of the final clean dataset: {df_popular.shape}")

            # Saving the cleaned data for transformation
            os.makedirs(self.data_validation_config.clean_data_dir,exist_ok=True)
            df_popular.to_csv(f"{self.data_validation_config.clean_data_dir}/{self.data_validation_config.clean_data_file}", index=False)
            logging.info(f"Cleaned data saved in {self.data_validation_config.clean_data_dir}")

            # Saving df_popular object for web app
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(df_popular,open(os.path.join(self.data_validation_config.serialized_objects_dir, "df_popular.pkl"),'wb'))
            logging.info(f"Saved final_rating serialization object to {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20} Data Validation log Started.{'='*20}")
            self.preprocess_data()
            logging.info(f"{'='*20} Data Validation log Completed.{'='*20}")
        except Exception as e:
            raise AppException(e, sys) from e
        