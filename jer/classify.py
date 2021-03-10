import numpy as np
import pandas as pd
df = pd.read_csv('jerus_final.csv')

category = []
df = df.replace(np.nan, '', regex=True)

df = df[~df['street'].str.contains('ספר')]
df = df[~df['street'].str.contains('תיכון')]
df = df[~df['street'].str.contains('מלון')]
df = df[~df['street'].str.contains('קבר')]
df = df[~df['street'].str.contains('גן')]
df = df[~df['street'].str.contains('גינה')]
df = df[~df['street'].str.contains('גינת')]
df = df[~df['street'].str.contains('גני')]
df = df[~df['street'].str.contains('בית כנסת')]
df = df[~df['street'].str.contains('בית הכנסת')]

df.to_csv('rest_jer.csv', encoding='utf-8-sig')


#category.to_csv('school_jerus.csv', encoding='utf-8-sig')
#knesset = df[df['street'].str.contains('מלון')]
# knesset.append(df[df['street'].str.contains('ביה"כ')])
#knesset = df[df['street'].str.contains('קבר')]
#knesset = df[df['street'].str.contains('גן')]
# knesset.append(df[df['street'].str.contains('גינה')])
# knesset.append(df[df['street'].str.contains('גינת')])
# knesset.append(df[df['street'].str.contains('גני')])

#category = df[df['street'].str.contains('ספר')]
# category.append(df[df['street'].str.contains('הספר')])
# category.append(df[df['street'].str.contains('בי"ס')])
# category.append(df[df['street'].str.contains('ביה"ס')])
# category.append(df[df['street'].str.contains('תיכון')])
# category.append(df[df['street'].str.contains('חטיבת')])
