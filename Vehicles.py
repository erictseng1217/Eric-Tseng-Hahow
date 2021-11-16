import pandas as pd
vehicles = {
    "name": ["name", "Speed"],
    "name": ['Sand Crawler', 'T-16 skyhopper', 'X-34 landspeeder', 'TIE/LN starfighter', 'Snowspeeder', 'TIE bomber', 'AT-AT', 'AT-ST', 'Storm IV Twin-Pod cloud car', 'Sail barge'],
    "Speed": [30, 1200, 250, 1200, 650, 850, 60, 90, 1500, 100]
}

df = pd.DataFrame(vehicles)

print("車輛列表：")
print(df)
print("=================================")
print("馬力超過1000的車輛：")
print(df[df['Speed'] > 1000])
