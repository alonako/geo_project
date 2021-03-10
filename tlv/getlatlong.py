import sys
from opencage.geocoder import OpenCageGeocode, RateLimitExceededError
import pandas as pd

key = '91fcb0b1ecdd4f598251608b2a93319f'
geocoder = OpenCageGeocode(key)
addressfile = 'addresses_utf8.txt'
longs = []
lats = []
df = pd.read_csv('tlv_table.csv')
i = 0
try:
    with open(addressfile, 'r', encoding="utf8") as f:

        for line in f:
            i += 1
            print(i)
            address = line.strip() + ' תל אביב '
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

except IOError:
    print('Error: File %s does not appear to exist.' % addressfile)
except RateLimitExceededError as ex:
    print(ex)

df.insert(10, 'long', pd.Series(longs), True)
df.insert(11, 'lat', pd.Series(lats), True)
df.to_csv('with_coors.csv', encoding='utf-8-sig')
