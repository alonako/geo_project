import pandas as pd
import os


city = "bs"
for filename in os.listdir(city):
    print(filename)
    if filename.endswith(".csv"):
        print(filename)
        file_path = os.path.join(city, filename)
        df = pd.read_csv(file_path)
        df['house number'] = df['house number'].fillna(0)
        address = []
        for index, row in df.iterrows():
            print(row['house number'])
            if row['house number'] != 0:
                address.append(row['street'] + " " + str(row['house number']))
            else:
                address.append(row['street'])

        df['street'] = address
        new_file_name = filename
        df.to_csv(new_file_name, encoding='utf-8-sig')
