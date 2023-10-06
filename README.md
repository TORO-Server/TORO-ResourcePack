# TORO-ResourcePack

TOROサーバーのリソースパック

## リソースパックのzipファイルの自動生成について

Pythonをインストールする必要があります。
（外部ライブラリは必要ない）

`zip.bat` または `zip.sh` を実行すると自動でリソースパックのzipファイルが生成されます。

zipファイルの生成が完了すると SHA-1 のハッシュ値がコンソールに表示されます。

`server.properties` の `resource-pack-sha1` の項目を表示されたハッシュ値にしてください。
