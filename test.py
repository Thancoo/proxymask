#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/26 8:52 下午
# @Author   : vadon
# @File     : test.py
# @Software : PyCharm


from settings import PGSQL_PASS_KEYS
from tools import net
from analysis.stream import Stream
from oracle import test
from oracle import one
from api import one as aa
from analysis import gg






b = b'\0xffhello, world'
# a = other.bytes2string(b)

print(test.Test)
print(one.Test)
print(aa.One)
print(gg.GoodGame)
print(Stream)

from queue import Queue, LifoQueue, PriorityQueue

q = Queue(maxsize=5)
lq = LifoQueue(maxsize=6)
pq = PriorityQueue(maxsize=5)

for i in range(5):
    q.put(i)
    lq.put(i)
    pq.put(i)


from phone import Phone

p = Phone()
a = p.find(18518920100)
print(a)


import ngender



from  pypinyin import Style, pinyin

a = pinyin('调情，拼音结果不会标明哪个韵母是轻声，轻声的韵母没有声调或数字标识')
print(a)




dd = '''{
    "id": "126202ee-4aef-ab1d-db66-cabb33cd1280",
    "type": "sparksql",
    "status": "available",
    "statementType": "text",
    "statement": "select+*+from+test.data_course+where+company=\"国家行政学院\"+limit+5",
    "aceCursorPosition": {
        "row": 0,
        "column": 0
    },
    "statementPath": "",
    "associatedDocumentUuid": null,
    "properties": {},
    "result": {
        "id": "010f776d-ee85-8b7b-63d5-c1d87b2aca16",
        "type": "table",
        "handle": {
            "log_context": null,
            "statements_count": 1,
            "end": {
                "column": 60,
                "row": 0
            },
            "statement_id": 0,
            "has_more_statements": false,
            "start": {
                "column": 0,
                "row": 0
            },
            "secret": "e0r3AT6ERfSAKLMHqnewaw==\n",
            "has_result_set": true,
            "session_guid": "Nmh4GeH8TOSOnJGpJCovKw==\n",
            "statement": "select+*+from+test.data_course+where+company=\"国家行政学院\"+limit+5",
            "operation_type": 0,
            "modified_row_count": null,
            "guid": "G5ZLIU2zTHaI8tLDm7Gtmg==\n",
            "previous_statement_hash": "022cff05b55a58fd5e273427461e16d758386bb7f2774d1c6ab7959e"
        }
    },
    "database": "default",
    "wasBatchExecuted": false
}'''

import json
print(json.loads(dd))



print(bytes(1))













