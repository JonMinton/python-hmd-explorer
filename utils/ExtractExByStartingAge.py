

import pandas as pd

def extractExByStartingAge(placesSelected, sexSelected, startingAge= 0):

        d = pd.read_csv("assets/data/lifetables.csv")

            # Need to change total value of sex to both
        sexSelectedAdjusted = 'both' if sexSelected == 'total' else sexSelected
        d2 = d.loc[
            (d['sex'] == sexSelectedAdjusted) & 
            (d['cntry'].isin(placesSelected)) & 
            (d['age'] == startingAge)
            , ['country', 'year', 'ex']
        ]
        # Not sure this is needed
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        
        d4 = d3.pivot(index='year', columns='country', values = 'ex')

        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()

        return yearSeries, countriesSeriesDict  
