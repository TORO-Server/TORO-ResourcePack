# TORO-ResourcePack

TOROサーバーのリソースパック

## リソースパックのzipファイルの自動生成について

GitHub Actions を利用してリソースパックのzipファイルを自動生成しています。

`zip.py` リソースパックのzipファイルを自動で生成する。

`sha1.sh` リソースパックのzipファイルのsha1のハッシュ値を出力する。

### リソースパックのURLについて

`server.properties` の `resource-pack` の項目を

```url
https://github.com/ユーザー名/リポジトリ名/blob/ブランチ名/ResourcePack.zip?raw=true
```

にしてください。

### サーバーリソースパックを変更した時にすること

リソースパックのzipファイルのコミットメッセージにsha1のハッシュ値が表示されます。

`server.properties` の `resource-pack-sha1` の項目を表示されたハッシュ値にしてください。
