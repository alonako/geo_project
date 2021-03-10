import sys
import pandas as pd
import csv
import pyproj
import requests

proj1 = pyproj.Proj(init='epsg:2039 ')  # ITM
proj2 = pyproj.Proj(init='epsg:4326')  # WGS84

wgs_longs = []
wgs_lats = []
df = pd.read_csv('jerus2.csv')

lngs = df['long']
lts = df['lat']

for i in range(0, len(lngs)):
    longitude, latitude = pyproj.transform(proj1, proj2, lngs[i], lts[i])
    print(longitude, latitude)
    wgs_longs.append(longitude)
    wgs_lats.append(latitude)

df.insert(4, 'long_wgs', pd.Series(wgs_longs), True)
df.insert(5, 'lat_wgs', pd.Series(wgs_lats), True)
df.to_csv('jerus2.csv', encoding='utf-8-sig')
