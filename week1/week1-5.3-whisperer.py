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


def whisperer():
    with open('resources/logo.jpg', mode='rb') as logo:
        contents = logo.read(1)
        result = ''
        while contents:
            y = repr(contents)[2:-1]
            x = re.sub(r'\\x[0-9A-Fa-f]{2}', '', str(y))
            x = re.sub(r'[^ \w\.]', '', x)
            if x.islower() or x == "!":
                result += x
            if len(result) > 4:
                yield result
                result = ''
            contents = logo.read(1)


for result in whisperer():
    print(result)
