import sys
import pandas as pd
import csv 

text_file = open("haifa comma.txt", encoding="utf8")
cleaned = []
i = 0
for x in text_file:
    if type(x) == str and ',' in x:
        x, y = x.split(",")[0], x.split(",")[1]
        cleaned.append(x + " " + y)
    else:
        print(i)


with open('addresses.txt', 'w', encoding="utf-8") as f:
    for item in cleaned:
        f.write("%s," % item)
