import pandas as pd
import pickle

df = pd.read_csv('assets/data/births.csv')

# print(df.head())

# print(df[['country', 'cntry']].head())

country_lookup = df[['country', 'cntry']].set_index('country').to_dict()['cntry']

# print(country_lookup)

with open('assets/lookups/countries.pkl', 'wb') as f:
    pickle.dump(country_lookup, f)
