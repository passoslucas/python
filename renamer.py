import os

os.chdir('\\Users\\lucas\\Desktop\\THE MANDALORIAN')

for f in os.listdir():
    f_name, f_ext = (os.path.splitext(f))
    f_title1, f_title2, f_ep, info1, info2, info3, info4 = (f_name.split('.'))

    f_title1 = f_title1.strip()
    f_title2 = f_title2.strip()
    f_ep = f_ep.strip()

    new_name = '{}-{}-{}{}'.format(f_ep, f_title1, f_title2, f_ext)

    os.rename(f, new_name)

#change the file name, cutting into pieces end chosing only the ones i want