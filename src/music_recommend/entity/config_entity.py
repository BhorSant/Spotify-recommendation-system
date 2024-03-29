from collections import namedtuple
DataIngetionConfig = namedtuple("DatasetConfig",["dataset_download_url",
                                                 "raw_data_dir",
                                                 "ingested_data_dir",])

DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                           "music_csv_file",
                                                           "spotify_csv_file",
                                                           "serialized_object_dir"])

DataTransformationConfig = namedtuple("DataTransformation",["clean_data_file_path",
                                                                   "transformed_data_dir"])  

ModelTrainingConfig = namedtuple("ModelTrainerConfig",["transformed_data_file_dir",
                                                       "trained_model_dir",
                                                       "trained_model_name"])

ModelRecommendationConfig = namedtuple("ModelRecommendationConfig", ["name_name_serialized_objects",
                                                      "music_pivot_serialized_objects",
                                                      "popularity_serialized_objects",
                                                      "trained_model_path"])
