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
    # ファイルへのフルパスを生成
    file_path = os.path.join(root, file)
    # ZipInfoオブジェクトを作成
    zip_info = zipfile.ZipInfo.from_file(file_path)

    # 時間の情報をリセット
    zip_info.date_time = (1980, 1, 1, 0, 0, 0)

    # ファイルをzipに追加
    with open(file_path, 'rb') as f:
        ziph.writestr(
            zip_info,
            f.read(),
            compress_type=zipfile.ZIP_DEFLATED,
            compresslevel=9
        )


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


# zipファイルに圧縮
zipf = zipfile.ZipFile(FILE_NAME, 'w', zipfile.ZIP_DEFLATED)
zipdir('.', zipf)
zipf.close()

# リソースパックの sha1 ハッシュ値を コンソールに出力
with open(FILE_NAME, 'rb') as file:
    print(hashlib.sha1(file.read()).hexdigest())
