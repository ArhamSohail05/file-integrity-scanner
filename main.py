import hashlib
from pathlib import Path
import json

found_hashes = "hashes.json"
dir_path = Path("/files")

def scan(file_path):
    pass

def find_files(dir_path):
    found = []

    for file_path in dir_path.iterdir():
        if file_path.is_file():
            found.append(file_path)
        else:
            found += find_files(file_path)

    return found

if __name__ == "__main__":
    files = find_files(dir_path)
    for f in files:
        scan(f)