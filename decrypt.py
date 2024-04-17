from utils.list_files import list_windows_files
from utils.crypt import decrypt_file
from utils.delete import secure_delete

# Define the key
KEY = 'b-7E2VRwcfvzraKw3LtGaiwKBsytCVz_4kA58PmTzGU='.encode('utf-8')

def main() -> None:
    for path in list_windows_files(directory_path='sample\\'):
        # 2nd step
        if path.endswith('.rawrr'):
            decrypt_file(path, KEY)
            secure_delete(path)

if __name__ == "__main__":
    main()