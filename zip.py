import os
import zipfile
import hashlib

# -----設定部分-----start

FORMAT = '%(asctime)s [%(levelname)s]:%(message)s'
FILE_NAME = 'ResourcePack.zip'
ALLOW_LIST = ["pack.mcmeta", "pack.png", "LICENSE", "README.md"]
DIRECTORY = "assets"

# -----設定部分-----end


def write(ziph: zipfile.ZipFile, root: str, file: str):
    ziph.write(os.path.join(root, file))


def zipdir(path: str, ziph: zipfile.ZipFile):
    for root, dirs, files in os.walk(path):
        dir = root.encode().decode()
        if (dir.startswith(DIRECTORY, 2)):
            for file in files:
                write(ziph, root, file)
        elif (dir == "."):
            for file in files:
                for allowFile in ALLOW_LIST:
                    if (file == allowFile):
                        write(ziph, root, file)
                        continue


zipf = zipfile.ZipFile(FILE_NAME, 'w', zipfile.ZIP_DEFLATED)
zipdir('.', zipf)
zipf.close()

with open(FILE_NAME, 'rb') as file:
    print(hashlib.sha1(file.read()).hexdigest())
