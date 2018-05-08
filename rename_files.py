import os

def rename():
    file_list = os.listdir(r"E:\Django Workspace\rename files") #directory where files are stored
    print(file_list)
    os.chdir(r"E:\Django Workspace\rename files")
    for file_name in file_list:
        print("Oldname - "+file_name)
        print("Newname - "+file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789"))
rename()
