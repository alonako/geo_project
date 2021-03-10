import json
import os

names = []
json_file_view = []
json_file_buildings = []
id_count = 0
with open('ramatgan.json') as f:
    data = json.load(f)
    for item in data['features']:
        properties = item['properties']
        geometry = item['geometry']
        coors = geometry['coordinates']
        lat = coors[1]
        long = coors[0]
        city = "ramat-gan"
        id = "rg" + str(id_count)
        name = properties['NAME']
        street = properties['adress']
        b_type = properties['TYPE_']
        year = str(properties['YEAR_'])
        if b_type == 'אתרי נוף':
            json_file = json_file_view
        else:
            json_file = json_file_buildings
        json_file.append({
            'city': city,
            'id': id,
            'name': name,
            'street': street,
            'b_type': b_type,
            'year': year,
            'geometry':  [lat, long]

        })
        id_count += 1
    with open("ramat-gan-buildings.json", 'w', encoding='utf-8') as f:
        json.dump(json_file_buildings, f, ensure_ascii=False, indent=4)
    with open("ramat-gan-view.json", 'w', encoding='utf-8') as f:
        json.dump(json_file_view, f, ensure_ascii=False, indent=4)
