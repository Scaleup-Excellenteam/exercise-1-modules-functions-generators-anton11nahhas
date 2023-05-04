import binascii
import re
from binascii import hexlify
"""
    this function opens a jpg file and reads it as binary, the
    goal is to extract the hidden message found in that binary 
    message, to do so we first read one byte remove the b prefix
    remove the hex bytes and finally remove all the /n /r /t 
    characters, check if the result is a lower case letter or !
    and store in result.
"""

import re

def extract_content(file_path):
    BYTES = 1024
    with open(file_path, 'rb') as f:
        # Read the file in chunks of 1024 bytes
        while True:
            chunk = f.read(BYTES)
            if not chunk:
                # End of file reached
                break
            # Search for secret messages in the chunk
            matches = re.findall(b'[a-z]{5,}!', chunk)
            for match in matches:
                # Decode the match from bytes to string
                msg = match.decode('utf-8')
                # Yield the secret message
                yield msg
def main():
    LOGO_PATH = 'resources/logo.jpg'
    generator = extract_content(LOGO_PATH)

    for message in generator:
        print(message)


if __name__ == '__main__':
    main()
