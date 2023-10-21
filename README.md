# TORO-ResourcePack

TORO サーバーのリソースパック

## リソースパックの zip ファイルの自動生成について

GitHub Actions を利用してリソースパックの zip ファイルを自動生成しています。

### ファイルの説明

`zip.py` リソースパックの zip ファイルを自動で生成して、リソースパックの sha1 の値をコンソールに出力する。

### リソースパックの URL について

`server.properties` の `resource-pack` の項目を

```url
https://github.com/ユーザー名/リポジトリ名/blob/ブランチ名/ResourcePack.zip?raw=true
```

にしてください。
