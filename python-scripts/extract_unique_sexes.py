import pandas as pd
import pickle

df = pd.read_csv('assets/data/births.csv')

# print(df.head())

lookup_sexes = df['sex'].unique()

with open('assets/lookups/sexes.pkl', 'wb') as f:
    pickle.dump(lookup_sexes, f)