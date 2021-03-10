import numpy as np
import pandas as pd
df = pd.read_csv('final_coors_tlv.csv')

category = []
df = df.replace(np.nan, '', regex=True)

category = df[df['shem_mivne'].str.contains('כנסת')]
df = df[~df['shem_mivne'].str.contains('כנסת')]
df.to_csv('rest_tlv.csv', encoding='utf-8-sig')


category.to_csv('bet-kneset_tlv.csv', encoding='utf-8-sig')
