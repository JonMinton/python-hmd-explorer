import pandas as pd
import numpy as np

def extract3dDataArrays(dataType, sexSelected, placeSelected):

    if dataType == "deaths":
        d = pd.read_csv("assets/data/deaths.csv")
        d2 = d.loc[
            (d['cntry'] == placeSelected) & 
            (d['sex'] == sexSelected) & 
            (d['age'] <= 90),
            :
        ]

        zArray = d2.loc[
            :, ['age', 'year', 'number_of_deaths']
        ].pivot(
            index = 'year', columns = 'age', values = 'number_of_deaths'
        )
        zArray = np.array(zArray)
        xRange = np.arange(d2['age'].min(), d2['age'].max())
        yRange = np.arange(d2['year'].min(), d2['year'].max())

        return xRange, yRange, zArray
    elif dataType == 'exposures':
        d = pd.read_csv("assets/data/exposures.csv")
        d2 = d.loc[
            (d['cntry'] == placeSelected) & 
            (d['sex'] == sexSelected) & 
            (d['age'] <= 90),
            :

        ]

        zArray = d2.loc[
            : , ['age', 'year', 'exposures_count']
        ].pivot(
            index = 'year', columns = 'age', values = 'exposures_count'
        )
        zArray = np.array(zArray)
        xRange = np.arange(d2['age'].min(), d2['age'].max())
        yRange = np.arange(d2['year'].min(), d2['year'].max())

        return xRange, yRange, zArray

    elif dataType == 'Mx':
        d = pd.read_csv('assets/data/Mx.csv')
        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'] == placeSelected) & 
            (d['age'] <= 90),
            :
        ]
        zArray = d2.loc[
            : , ['age', 'year', 'mx']
        ].pivot(
            index = 'year', columns = 'age', values = 'mx'
        )
        zArray = np.array(zArray)
        xRange = np.arange(d2['age'].min(), d2['age'].max())
        yRange = np.arange(d2['year'].min(), d2['year'].max())

        return xRange, yRange, zArray
    elif dataType == 'population':
        print("Extracting population count data")
        d = pd.read_csv('assets/data/population.csv')
        print(d.head())
        d2 = d.loc[
            (d['sex'] == sexSelected) & 
            (d['cntry'] == placeSelected) & 
            (d['age'] <= 90),
            :
        ]
        zArray = d2.loc[
            : , ['age', 'year', 'population_count']
        ].pivot(
            index = 'year', columns = 'age', values = 'population_count'
        )
        zArray = np.array(zArray)
        xRange = np.arange(d2['age'].min(), d2['age'].max())
        yRange = np.arange(d2['year'].min(), d2['year'].max())

        return xRange, yRange, zArray
    elif dataType == 'lifetables':
        print("Extracting lifetables data")
        d = pd.read_csv("assets/data/lifetables.csv")
        print(d.head())
        sexSelectedAdjusted = 'both' if sexSelected == 'total' else sexSelected       

        d2 = d.loc[
                    (d['sex'] == sexSelectedAdjusted) & 
                    (d['cntry'] == placeSelected) & 
                    (d['age'] <= 90),
                    :
                ]
        zArray = d2.loc[
            : , ['age', 'year', 'ex']
        ].pivot(
            index = 'year', columns = 'age', values = 'ex'
        )
        zArray = np.array(zArray)
        xRange = np.arange(d2['age'].min(), d2['age'].max())
        yRange = np.arange(d2['year'].min(), d2['year'].max())

        return xRange, yRange, zArray