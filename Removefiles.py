import os, shutil, time
source = input("Enter the path of the file/folder")#path actual
Time = float(input("Enter the time till which you want to keep the file/folder"))

def RemoveFiles():
    if(os.path.exists(source)):
        sec = time.time(Time)

        list = os.walk(source)
        ctime = os.stat(list).st_ctime

        if(ctime > sec):
            if(os.path.isfile(source)):
                os.remove(source)
            else:
                shutil.rmtree(source)
    else:
        print("Path does not exist")

RemoveFiles()