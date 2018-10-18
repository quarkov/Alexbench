from os import chdir, mkdir, listdir, getcwd
from datetime import*


def store_dir(hostname):

    if "results" not in listdir():
        mkdir("results")
    chdir("results")

    hs = hostname.replace("/", ".")

    if hs not in listdir():
        mkdir(hs)
    chdir(hs)

    if str(len(listdir())+1) not in listdir():
        index = str(len(listdir())+1)
        mkdir(str(len(listdir())+1))
    chdir(str(len(listdir())))

    filename = hs.split(".")[0] + "_" + str(datetime.now()).split()[0] + "_" + index
    return filename
