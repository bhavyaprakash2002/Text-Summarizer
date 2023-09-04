import os
import urllib.request as request
import zipfile
from text_summarizer.logging import logger
from text_summarizer.utils.common import get_size
#import zipfile36 as zipfile
import py7zr
from pathlib import Path
from text_summarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # zip_file_path = "artifacts/data_ingestion/data.zip"  # Replace with the actual path to your ZIP file

        
        with py7zr.SevenZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  # Replace "destination_folder" with the folder where you want to extract the files
        # except py7zr.exceptions.Bad7zFile:
        #     print("The file is not a valid 7z archive.")
        # except FileNotFoundError:
        #     print(f"The file '{zip_file_path}' does not exist.")

        # with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
        #     zip_ref.extractall(unzip_path)
 