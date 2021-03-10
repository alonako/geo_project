import sys
from opencage.geocoder import OpenCageGeocode, RateLimitExceededError
import pandas as pd

key = '91fcb0b1ecdd4f598251608b2a93319f'
geocoder = OpenCageGeocode(key)
addressfile = 'addresses.txt'
longs = []
lats = []
df = pd.read_csv('haifa.csv')
i = 0
try:
    with open(addressfile, 'r', encoding="utf8") as f:

        for line in f:
            i += 1
            address = line.strip() + ' חיפה '
            results = geocoder.geocode(
                address, no_annotations='1', country='il', language='he')

            if results and len(results):
                longitude = results[0]['geometry']['lng']
                latitude = results[0]['geometry']['lat']
                longs.append(longitude)
                lats.append(latitude)
                print(latitude, longitude)
            else:
                sys.stderr.write("not found \n")
                longs.append('none')
                lats.append('none')

except IOError:
    print('Error: File %s does not appear to exist.' % addressfile)
except RateLimitExceededError as ex:
    print(ex)

df.insert(2, 'long', pd.Series(longs), True)
df.insert(3, 'lat', pd.Series(lats), True)
df.to_csv('with_coors.csv', encoding='utf-8-sig')
