from os import chdir, makedirs, mkdir, listdir, path
from datetime import*


def store_dir(hostname):
    today = str(datetime.now()).split()[0]
    local_path = path.join(".", "results", hostname, today)
    makedirs(local_path, exist_ok=True)
    chdir(local_path)
    index = "0"
    for i in range(1,len(listdir('.'))+2):
        if str(i) not in listdir('.'):
            index = str(i)
            mkdir(index)
            chdir(index)
            break
    filename = hostname.split(".")[0] + "_" + today + "_" + index
    return filename
