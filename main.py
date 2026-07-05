import hashlib
from pathlib import Path
import json

found_hashes = "hashes.json"
dir_path = Path("files/")

def scan(file_path):
    with open(file_path, "rb") as f:
        d = hashlib.file_digest(f, "sha256")
        digest = d.hexdigest()

    file_path = str(file_path)

    with open("hashes.json", "r") as hashes:
        try:
            data = json.load(hashes)        
        except json.JSONDecodeError:
            print("File was empty or corrupted. Proceeding with empty file:")
            data = {}
    
    if file_path in data and data[file_path] == digest:
        print(file_path + " not modified.")
    elif not file_path in data:
        data[file_path] = digest
        print("Added " + file_path + ".")
    else:
        data[file_path] = digest
        print(file_path + " was modified. Storing new file hash.")

    with open("hashes.json", "w") as file:
        json.dump(data, file, indent=4)


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