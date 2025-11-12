#Create a tar file

import tarfile

# with tarfile.open("archieve.tar","w") as t:
#     t.add("Example2.py")
# print("file added to tar archieve")

# with tarfile.open("archieve.tar","r") as t:
#     print("contents:",t.getnames())
    
#Extract all files
with tarfile.open("archieve.tar","r") as t:
    t.extractall("tar_extracted")
print("File extracted successfully")