import os

os.chdir('\\Users\\lucas\\Desktop\\mando')

for f in os.listdir():
    f_name, f_type = (os.path.splitext(f))
    new_name = f_name = f_name.upper()

    os.rename(f, new_name)

#putting the file name to UPPERCASE
