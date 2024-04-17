'''
This util is created to list the files inside the windows system
as fast and quickly as possible
'''

from concurrent.futures import ThreadPoolExecutor, as_completed
from os import scandir

def list_files_single_thread(directory_path):
    try:
        with scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    yield entry.path
                elif entry.is_dir():
                    yield from list_files_single_thread(entry.path)
    except Exception as e:
        print(e)

def list_windows_files(directory_path='C:\\'):
    # Pool size depends on your hardware and specific use case
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_dir = {executor.submit(list_files_single_thread, path): path for path in [directory_path]}
        for future in as_completed(future_to_dir):
            yield from future.result()