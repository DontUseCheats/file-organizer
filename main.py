import os
import shutil
import json
from pathlib import Path

# create a categories Dict which contains all filetypes
FILES_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Videos": {".mp4", ".mov", ".avi", "mkv"},
    "Audio": {".mp3", ".wav", ".flac", ".aac"},
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Archives": {".zip", ".tar", ".gz", ".rar"}
}

# create tuples list to define size range of file
SIZE_BUCKETS = [
    ("Small", 0,                1_048_576),
    ("Medium", 1_048_576,       104_857_600),
    ("Large", 104_857_600,      1_073_741_824),
    ("Huge", 1_073_741_824,     float("inf"))
]

# create lookup functions for each feature
# function parameter is passed from call
def get_category(file_type):
    for category, extensions in FILES_CATEGORIES.items():
        if file_type in extensions:
            return category
        return "Other"

def get_size_bucket(size_bytes):
    for category, low_range, high_range in SIZE_BUCKETS:
        if low_range <= size_bytes < high_range:
            return category

# create scan for specific file
# "folder" is folder path user wants to look at
# "sort_by" is whether to sort by type, size or both
def organize_file(folder, sort_by):
    folder = Path(folder)
    moves = []   # track every move

    for file in folder.iterdir():
        if file.is_file():
            category = get_category(file.suffix)
            size_bucket = get_size_bucket(file.stat().st_size)


            # creates subfolder pathways in destination path
            if sort_by == "type":
                subfolder = folder / category
            elif sort_by == "size":
                subfolder = folder / size_bucket
            else: # both
                subfolder = folder / category / size_bucket

            # creates actual folder on disk
            subfolder.mkdir(parents=True, exist_ok=True)
            destination = subfolder / file.name
            shutil.move(str(file), str(destination)) # moves file to according destination
            moves.append({"from": str(file), "to": str(destination)})

            log_path = folder / ".organizer_log.json"
            with open(log_path, "w") as f:
                json.dump(moves, f)




# argparse to identify which file directory to look