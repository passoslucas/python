import os

path = os.chdir("C:\\Users\\lucas\\Desktop\\newfolder")
x = 0

for file in os.listdir(path):
    new_file_name = "file{}.txt".format(x)
    os.rename(file, new_file_name)

    x += 1

#rename a file by puting a counting number a side the name
