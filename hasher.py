import os
import hashlib

def hash_file(filepath, hash_type="sha256"):
    """Hashes a file and overwrites it with the hash."""
    hash_functions = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha224": hashlib.sha224,
        "sha256": hashlib.sha256,
        "sha384": hashlib.sha384,
        "sha512": hashlib.sha512
    }

    if hash_type not in hash_functions:
        print(f"Invalid hash type: {hash_type}")
        return

    try:
        with open(filepath, "rb") as file:
            file_data = file.read()
            hashed_data = hash_functions[hash_type](file_data).hexdigest()

    
        with open(filepath, "w") as file:
            file.write(hashed_data)

        print(f"Hashed {filepath} and replaced its contents.")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def hash_files_in_directory(directory, hash_type="sha256"):
    """Recursively hashes all files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            hash_file(filepath, hash_type)



target_directory = "test_folder"
hash_files_in_directory(target_directory)
