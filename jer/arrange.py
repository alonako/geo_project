import pandas as pd
import json
import os


cities = ["jer"]
count = 0
for city in cities:
    for filename in os.listdir(city):
        if filename.endswith(".csv"):
            ids = []
            print(filename)
            file_path = os.path.join(city, filename)
            df = pd.read_csv(file_path)
            rows = df.shape[0]
            for i in range(0, rows):
                ids.append("j" + str(count))
                count += 1
            df['name'] = ''
            df['city'] = 'jerusalem'
            df['id'] = ids
        df.to_csv(filename, encoding='utf-8-sig')
