import os
import shutil

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

def get_size_buckets(size_bytes):
    for category, low_range, high_range in SIZE_BUCKETS:
        if low_range <= size_bytes < high_range:
            return category



# create scan for file directory