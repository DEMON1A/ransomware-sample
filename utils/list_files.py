'''
This util is created to list the files inside the windows system
as fast and quickly as possible
'''

from concurrent.futures import ThreadPoolExecutor, as_completed
from os import scandir

def list_files_single_thread(directory_path):
    # Define directories to ignore
    ignore_dirs = ['C:\\Windows', 'C:\\Boot']
    try:
        with scandir(directory_path) as entries:
            for entry in entries:
                # Check if the directory is not in the list of directories to ignore
                if entry.is_dir():
                    full_path = entry.path
                    if full_path not in ignore_dirs:
                        yield from list_files_single_thread(full_path)
                elif entry.is_file():
                    yield entry.path
    except Exception as e:
        print(f"Error accessing {directory_path}: {e}")

def list_windows_files(directory_path='C:\\'):
    # Pool size depends on your hardware and specific use case
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_dir = {executor.submit(list_files_single_thread, directory_path): directory_path}
        for future in as_completed(future_to_dir):
            yield from future.result()