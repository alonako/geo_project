import sys
from opencage.geocoder import OpenCageGeocode, RateLimitExceededError
import pandas as pd

key = '91fcb0b1ecdd4f598251608b2a93319f'
geocoder = OpenCageGeocode(key)
df_add = pd.read_csv('address.csv')
addresses = df_add['street']
longs = []
lats = []
df = pd.read_csv('bs.csv')
i = 0
for line in addresses:
    i += 1
    print(i)
    address = line.strip() + ' באר שבע '
    results = geocoder.geocode(
        address, no_annotations='1', country='il', language='he')

    if results and len(results):
        longitude = results[0]['geometry']['lng']
        latitude = results[0]['geometry']['lat']
        print(longitude, latitude)
        longs.append(longitude)
        lats.append(latitude)

    else:
        sys.stderr.write("not found \n")
        longs.append('none')
        lats.append('none')

df.insert(5, 'long', pd.Series(longs), True)
df.insert(6, 'lat', pd.Series(lats), True)
df.to_csv('bs_with_coors.csv', encoding='utf-8-sig')
