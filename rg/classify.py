import json
import os

names = []
people_rg = []
hotel_rg = []
school_rg = []
bet_knesset_rg = []
museum_rg = []
json_file = []
rest_rg = []
count_items = 0
count = 0
schools = ["בית ספר","בית הספר","תיכון","חטיבה","חטיבת","בי\"ס"]
rest = True
with open('ramat-gan-buildings.json') as f:
            data = json.load(f)
            
            for item in data:
                count_items+=1
                name = item['name']
                names.append(name)
                for s in schools:
                    if s in name:
                        school_rg.append(item)
                        count+=1
                        rest = False
                if 'כנסת' in name:
                    bet_knesset_rg.append(item)
                    count+=1
                elif 'מלון' in name:
                    hotel_rg.append(item)
                    count+=1
                elif 'מוזיאון' in name:
                    museum_rg.append(item)  
                    count+=1
                elif 'בית' in name:
                    people_rg.append(item)
                    count+=1
                elif rest:
                    rest_rg.append(item)
                    count+=1
                    
                          
            json_file.append({
                    'people_rg': people_rg,
                    'hotel_rg': hotel_rg,
                    'school_rg': school_rg,
                    'bet_knesset_rg': bet_knesset_rg,
                    'museum_rg': museum_rg,
                    'rest_rg' : rest_rg
                    })
                
print(count)
print(count_items)
with open("rg_new.json", 'w', encoding='utf-8') as f:
                json.dump(json_file, f, ensure_ascii=False, indent=4)