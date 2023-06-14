#!python3.11
import datetime as dt
import re

s = '2022-12-30T16:27:56.9871548+08:00'
print(dt.datetime.fromisoformat(s))
# 2022-12-30 16:27:56.987154+08:00