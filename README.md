# COVID19 Scraping Script for Osaka

## What's this?
大阪府の公開する情報を[大阪府 新型コロナウイルス対策サイト](https://covid19-osaka.info/)向けに整形し、
json形式にまとめ、出力するスクリプトです。  
自動生成したdata.jsonは参照データであるExcelファイルとともに[GitHub Pagesブランチ](https://github.com/y-chan/covid19osaka-scraping/tree/gh-pages)にアップロードされます。
(GitHub Actionsで1時間毎に自動実行しています。)

## Make date
元データとなるExcelファイル (patients_and_inspections.xlsx, contacts1.xlsx, contacts2.xlsx) を ./data/ フォルダに配置して実行すると、 ./data/ に data.json が出力されます。
```shell script
pip install -r requirements.txt
python3 main.py
```

## License
このスクリプトは[MITライセンス](LICENSE)で公開されています。
