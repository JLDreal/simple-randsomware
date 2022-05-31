import os
import scandir
from cryptography.fernet import Fernet
folder = os.path.expandvars("%userprofile%")+"/Pictures/Camera Roll" #can be changed to fit your needs

file_list = []
i=0
for paths, dirs, files in scandir.walk(folder):
    for file in files:
        if file.endswith("encrypt.py" or "decrypt.py" or "thekey.key"):
            continue
        else:
            file_list.append(os.path.join(paths, file))
#win11 ghostfilefilter
while i <= len(file_list)-1:
    file_path = file_list[i]
    if file_path.endswith("ini"):
        file_list.remove(file_list[i])
    i=i+1
#end of ghostfilefilter

with open("thekey.key", "rb") as thekey:
    secretkey = thekey.read()

for file in file_list:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

