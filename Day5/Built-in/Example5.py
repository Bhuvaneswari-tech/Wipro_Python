#Create a Zip file

import zipfile

#Create a ZIP archieve and adds the existing file
# with zipfile.ZipFile("files.zip","w") as z:
#     z.write("Example4.py")
#     z.write("Example1.py")
#     z.write("Example2.py")
# print("3 files added to files.zip")

#display the list of files in the ZIP archieve
# with zipfile.ZipFile("files.zip","r") as z:
#     print("Contents: ",z.namelist())
    
#Extract all the files
with zipfile.ZipFile("files.zip","r") as z:
    z.extractall("extracted")
print("All files extracted to folder")
