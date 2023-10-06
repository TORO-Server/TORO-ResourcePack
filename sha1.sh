#!/bin/bash

# ファイル名
file="ResourcePack.zip"

# ハッシュ値 (sha1) を出力
echo $(sha1sum $file) | awk '{print $1}'
