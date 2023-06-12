import pandas as pd


def extract2dDataSeries(datatypeSelected, placesSelected, sexSelected):

    if datatypeSelected == 'births':
        d = pd.read_csv("assets/data/births.csv")

        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'].isin(placesSelected))
            , ['country', 'year', 'number_of_births']
        ]
        # The following is for cases where more than one value is availbale for 
        # a particular sex and country combination
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        d4 = d3.pivot(index='year', columns='country', values = 'number_of_births')
        
        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()

        return yearSeries, countriesSeriesDict
    elif datatypeSelected == 'deaths':
        d = pd.read_csv("assets/data/deaths.csv")

        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'].isin(placesSelected))
            ,
            ['country', 'year', 'number_of_deaths']
        ]
        
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        d4 = d3.pivot(index='year', columns='country', values = 'number_of_deaths')
        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()

        return yearSeries, countriesSeriesDict
    elif datatypeSelected == 'exposures':
        d = pd.read_csv("assets/data/exposures.csv")

        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'].isin(placesSelected))
            , ['country', 'year', 'exposures_count']
        ]
        
        # The following is for cases where more than one value is availbale for 
        # a particular sex and country combination
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        d4 = d3.pivot(index='year', columns='country', values = 'exposures_count')
        
        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()

        return yearSeries, countriesSeriesDict
        
    elif datatypeSelected == 'mx':
        d = pd.read_csv("assets/data/Mx.csv")
        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'].isin(placesSelected))
            , ['country', 'year', 'mx']
        ]
        
        # The following is for cases where more than one value is availbale for 
        # a particular sex and country combination
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        d4 = d3.pivot(index='year', columns='country', values = 'mx')
        
        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()
        
        return yearSeries, countriesSeriesDict
    elif datatypeSelected == 'population':
        d = pd.read_csv("assets/data/population.csv")

        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'].isin(placesSelected))
            , ['country', 'year', 'population_count']
        ]
        
        # The following is for cases where more than one value is availbale for 
        # a particular sex and country combination
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        d4 = d3.pivot(index='year', columns='country', values = 'population_count')
        
        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()
        
        return yearSeries, countriesSeriesDict

    elif datatypeSelected == 'lifetables':
        d = pd.read_csv("assets/data/lifetables.csv")

            # Need to change total value of sex to both
        sexSelectedAdjusted = 'both' if sexSelected == 'total' else sexSelected
        d2 = d.loc[
            (d['sex'] == sexSelectedAdjusted) & 
            (d['cntry'].isin(placesSelected)) & 
            (d['age'] == 0)
            , ['country', 'year', 'ex']
        ]
        
        d3 = d2.groupby(['country', 'year']).agg('mean').reset_index()
        
        d4 = d3.pivot(index='year', columns='country', values = 'ex')

        yearSeries = d4.index.to_list()
        countriesSeriesDict = d4.to_dict()

        return yearSeries, countriesSeriesDict  

