# from dagster import materialize
# from Ashkan.Ashkan.assets import cereals
# if __name__ == "__main__":
#     materialize([cereals])


import pandas as pd



df = pd.read_csv("/external/test_proj/dagster/cereals.csv",index_col=False)
df.set_index('name',inplace=True)
mask = df['calories'] > 110
df = df.loc[mask,['calories']]

print("==>> df: ", df)