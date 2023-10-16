# TORO-ResourcePack

TOROサーバーのリソースパック

## リソースパックのzipファイルの自動生成について

GitHub Actions を利用してリソースパックのzipファイルを自動生成しています。

コミットメッセージにsha1のハッシュ値が書かれます。

### ファイルの説明

`zip.py` リソースパックのzipファイルを自動で生成して、リソースパックのsha1の値をコンソールに出力する。


### リソースパックのURLについて

`server.properties` の `resource-pack` の項目を

```url
https://github.com/ユーザー名/リポジトリ名/blob/ブランチ名/ResourcePack.zip?raw=true
```

にしてください。
