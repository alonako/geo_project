import pandas as pd
import numpy as np
# city, id, name, street, b_type, lat, long
df = pd.read_csv('beer-sheva.csv', encoding='utf-8')
df = df.replace(np.nan, '')

streets = df['street']
comments = df['comments']

rev_streets = []
rev_comments = []


for street in streets:
    rev_streets.append(street[::-1])

for comment in comments:
    cm = str(comment)
    if(cm == None):
        rev_comments.append(" ")
    else:
        rev_comments.append(cm[::-1])

df['street'] = rev_streets
df['comments'] = rev_comments

df.to_csv('bs.csv', encoding='utf-8-sig')
