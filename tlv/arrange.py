import pandas as pd

df = pd.read_csv('tlv_table.csv')
addresses = df['ktovot']
list_addreses = addresses.tolist()
print(len)
cleaned = []
for x in list_addreses:
    if type(x) == str and ',' in x:
        x = x.split(",")[0]
        print(x)

    cleaned.append(x)

with open('addresses.txt', 'w') as f:
    for item in cleaned:
        f.write("%s,\n" % item)