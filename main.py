from pathlib import Path
import shutil
import time
from datetime import datetime
import argparse

class OldFilesArchiver:

    """
      This very easy project automates the process of archiving files which are older
      than a specified number of days. The user can arbitrarily set the number of days
      as the threshold for archiving. Files exceeding the specified age will be automatically 
      moved to a newly created archive folder, thus preserving the data.
    """

    def __init__(self, source_folder, age_limit_days):

        self.source_folder = Path(source_folder)
        self.age_limit_days = age_limit_days
        self.archive_folder = self.source_folder / "archive_folder"
        self.log_folder = self.source_folder / "log_folder"
        self.log_folder.mkdir(parents=True, exist_ok=True)
        self.archive_folder.mkdir(parents=True, exist_ok=True)
        self.log_file = Path(self.log_folder) / "archive_log.txt" 
    
    
    """
      log_action will report every action will happen during the synchronization,
      whether a file has been copied, deleted or updated.
    """
     
    def log_action(self, message):
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(self.log_file, 'a') as f: f.write(f"{current_time}: {message}\n")
    
    

    def oldfiles_archiver(self, source_folder=None):
        
        current_time = time.time()

        source_folder = Path(source_folder or self.source_folder)

        if not source_folder.exists():

            raise FileNotFoundError(f"Source folder does not exist: {source_folder}")

        for file in source_folder.iterdir():

            file_mod_time = file.stat().st_mtime

            file_age_days = (current_time - file_mod_time) / (24 * 60 * 60)

            if file.is_file():
                

                if file_age_days > self.age_limit_days:
            
                    try: 

                        shutil.move(str(file),str(self.archive_folder / file.name))
                
                        self.log_action(f"'{file.name}' has been successfully moved into archive folder")
           
                    except Exception as e:

                        self.log_action(f"Failed to archive {file.name}: {str(e)}")

            elif file.is_dir():

                self.oldfiles_archiver(file)

def parse_arguments():

    parser = argparse.ArgumentParser(description = "Old Files Archiver")

    parser.add_argument("source_folder", type = str)

    parser.add_argument("age_limit_days", type = int)

    return parser.parse_args()

if __name__ == "__main__":

    args = parse_arguments()

    OldFilesArchiver = OldFilesArchiver(args.source_folder, args.age_limit_days)

    OldFilesArchiver.oldfiles_archiver()
        
