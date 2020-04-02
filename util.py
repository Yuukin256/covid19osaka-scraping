import openpyxl
import requests
import codecs
import shutil
import time

from datetime import datetime, timedelta, timezone
from json import dumps

from typing import Dict

jst = timezone(timedelta(hours=9), 'JST')

MAIN_SUMMARY_INIT = {
    "attr": "検査実施人数",
    "value": 0,
    "children": [
        {
            "attr": "陽性患者数",
            "value": 0,
            "children": [
                {
                    "attr": "入院／入院調整中",
                    "value": 0,
                    "children": [
                        {
                            "attr": "軽症・中等症",
                            "value": 0
                        },
                        {
                            "attr": "重症",
                            "value": 0
                        }
                    ]
                },
                {
                    "attr": "退院",
                    "value": 0
                },
                {
                    "attr": "死亡",
                    "value": 0
                }
            ]
        }
    ]
}


def excel_date(num) -> datetime:
    return datetime(1899, 12, 30) + timedelta(days=num, hours=8)


def get_xlsx(filename: str) -> openpyxl.workbook.workbook.Workbook:
    return openpyxl.load_workbook("./data/" + filename)


def dumps_json(file_name: str, json_data: Dict) -> None:
    with codecs.open("./data/" + file_name, "w", "utf-8") as f:
        f.write(dumps(json_data, ensure_ascii=False, indent=4, separators=(',', ': ')))
