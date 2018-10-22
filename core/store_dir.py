from os import chdir, mkdir, listdir, getcwd
from datetime import*


def store_dir(hostname):
    today = str(datetime.now()).split()[0]
    folder_seq = ["results", hostname, today]
    for folder in folder_seq:
        if folder not in listdir('.'):
            mkdir(folder)
        chdir(folder)
    index = "0"
    for i in range(1,len(listdir('.'))+2):
        if str(i) not in listdir('.'):
            index = str(i)
            mkdir(index)
            chdir(index)
            break

    filename = hostname.split(".")[0] + "_" + today + "_" + index
    return filename
