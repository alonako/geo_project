import pandas as pd
import json
import os

# city, id, name, street, b_type, lat, long
cities = ["haifa", "tlv", "jer"]
for city_dir in cities:
    for filename in os.listdir(city_dir):
        if filename.endswith(".csv"):
            print(os.path.join(city_dir, filename))
            file_path = os.path.join(city_dir, filename)
            df = pd.read_csv(file_path)
            json_file = []
            for index, row in df.iterrows():
                city = '' if type(row['city']) != str else row['city']
                id = '' if type(row['id']) != str else row['id']
                name = '' if type(row['name']) != str else row['name']
                street = '' if type(row['street']) != str else row['street']
                b_type = '' if type(row['b_type']) != str else row['b_type']

                if type(row['lat']) != int or type(row['long']) != int:
                    pass

                json_file.append({
                    'city': city,
                    'id': id,
                    'name': name,
                    'street': street,
                    'b_type': b_type,
                    'geometry':  [row['lat'], row['long']]
                })
            json_fname = filename[:-4] + ".json"
            with open(json_fname, 'w', encoding='utf-8') as f:
                json.dump(json_file, f, ensure_ascii=False, indent=4)
