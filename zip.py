import os
import zipfile
import hashlib

# -----設定部分-----start

FILE_NAME = 'ResourcePack.zip'
ALLOW_LIST = ["pack.mcmeta", "pack.png", "LICENSE", "README.md"]
DIRECTORY = "assets"

# -----設定部分-----end


def writeDir(zipf: zipfile.ZipFile, dir_path: str):
    for item in sorted(os.listdir(dir_path)):
        target_path = os.path.join(dir_path, item)

        if os.path.isfile(target_path):
            writeFile(zipf, target_path)
        else:
            writeDir(zipf, target_path)


def writeFile(zipf: zipfile.ZipFile, file_path: str):
    # ZipInfoオブジェクトを作成
    zip_info = zipfile.ZipInfo.from_file(file_path)

    # 時間の情報をリセット
    zip_info.date_time = (1980, 1, 1, 0, 0, 0)
    # ファイルのアクセス権を777に設定
    zip_info.external_attr = 0o777 << 16
    # 拡張フィールドを削除
    zip_info.extra = b""

    # ファイルをzipに追加
    with open(file_path, 'rb') as f:
        zipf.writestr(
            zip_info,
            f.read(),
            compress_type=zipfile.ZIP_DEFLATED,
            compresslevel=9
        )


def zipdir(path: str, zipf: zipfile.ZipFile):
    for target_path in sorted(os.listdir(path)):
        if os.path.isfile(target_path):
            if target_path in ALLOW_LIST:
                writeFile(zipf, target_path)
        elif target_path == DIRECTORY:
            writeDir(zipf,  target_path)


# zipファイルに圧縮
with zipfile.ZipFile(FILE_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('.', zipf)

# リソースパックの sha1 ハッシュ値を コンソールに出力
with open(FILE_NAME, 'rb') as file:
    print(hashlib.sha1(file.read()).hexdigest())
