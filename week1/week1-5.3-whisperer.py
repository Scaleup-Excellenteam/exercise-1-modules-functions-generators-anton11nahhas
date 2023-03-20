import binascii


def anxious():
    with open('resources/logo.jpg', encoding="utf8", errors='ignore') as logo:
        contents = logo.read()
    yield contents


for result in anxious():
    print(result)
