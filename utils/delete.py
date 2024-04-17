'''
This util is created to secure delete files where it can't be recovered
ever again using the file shredding technique
'''

import os
import random

def secure_delete(file_path, passes=3):
    if not os.path.isfile(file_path):
        raise ValueError("File not found: " + file_path)

    # Get the size of the file and overwrite it multiple times
    with open(file_path, "r+b") as file:
        length = os.path.getsize(file_path)
        for _ in range(passes):
            file.seek(0)
            # Write random bytes to scramble the file data
            file.write(random.randbytes(length))

    # Optionally, rename the file to obscure the original file name
    temp_name = file_path + ".deleted"
    os.rename(file_path, temp_name)

    # Delete the file
    os.remove(temp_name)