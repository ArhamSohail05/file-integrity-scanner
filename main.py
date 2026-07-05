import hashlib
from pathlib import Path
import json

found_hashes = "hashes.json"
dir_path = Path("/files")

def scan(file_path):
    digest = hashlib.file_digest(file_path, "sha256")

    with open("hashes.json", "r") as hashes:
        data = json.load(hashes)
    
    if data[file_path] and data[file_path] == digest:
        print(file_path + " not modified.")
    elif not data[file_path]:
        data[file_path] = digest
        print("Added " + file_path + ".")
    else:
        data[file_path] = digest
        print(file_path + " was modified. Storing new file hash.")


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