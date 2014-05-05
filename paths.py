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