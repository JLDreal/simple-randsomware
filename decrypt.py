import os
import scandir
from cryptography.fernet import Fernet
folder = os.path.expandvars("%userprofile%")+"/Pictures/Camera Roll" #last part changeable

file_list = []

for paths, dirs, files in scandir.walk(folder):
    for file in files:
        if file.endswith("encrypt.py" or "decrypt.py" or "thekey.key"):
            continue
        else:
            file_list.append(os.path.join(paths, file))

#weird win11 File thing idk
if (folder+"\\desktop.ini") in file_list:
    file_list.remove(folder+"\\desktop.ini")
else:
    print(file_list)
#end of that

with open("thekey.key", "rb") as thekey:
    secretkey = thekey.read()

for file in file_list:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
