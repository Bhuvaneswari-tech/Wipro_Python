#os module allows interation with the operating system

import os

#Get current working directory
print("Current Directory:",os.getcwd())

#List files in directory
print("Files and folders:",os.listdir('.'))

#create a new directory
os.makedirs('test_folder',exist_ok=True)
print("Directory 'test folder' created!")

#check if a file exists
print("Does file exist?", os.path.exists('Example1.py'))

#Remove a directory
