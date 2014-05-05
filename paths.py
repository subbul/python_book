import os

os.listdir(".") #list files in current directory

print(os.getcwd()) #prints current working directory

os.chdir("e:\Programming\python\quickPythonBook")
print(os.listdir(".")) #prints files in newly CD-ed directory

print(os.path.join("bin","utils","disktools")) #joins all the elements with correct seperator like /bin/utils/disktools

print(os.path.split("some/directory/file")) #splits into two element tuple with first element
#pointintg to the direcoty,second element points to the file name itself

print(os.path.basename("some/directory/file.jpg"))#returs only the file element
print(os.path.dirname("some/directory/file.jpg"))#return directory name

print(os.path.splittext("abc.jpeg")) #returns tuple containing filename and its extension

print(os.name()) #returns 'nt' for windows based system

print(os.path.exists("C:\Unknown")) #should return false
print(os.path.exists("C:\windows")) #should return true
print(os.path.isfile("C:\Windows\AppPatch\AcRes.dll")) #should retunr true as this file exists

import glob
glob.glob("*") # returns all files - wildcard
glob.glob("*.py") #returns only .py files


#os walk