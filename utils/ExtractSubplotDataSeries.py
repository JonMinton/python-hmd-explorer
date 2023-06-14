import pandas as pd
import numpy as np


def extractSubplotDataSeries(typeValue, placeValue, sexValue, ageValue, yearValue):
    print("In extractSubplotDataSeries")
    cohortValue = yearValue - ageValue

    if typeValue == 'deaths':
        print("typevalue deaths detected")
        d = pd.read_csv("assets/data/deaths.csv")
        print(d.head())
        dAge = d.loc[
            (d['sex'] == sexValue) &
            (d['cntry'] == placeValue) & 
            (d['age'] == ageValue),
            ['year', 'number_of_deaths'] 
        ]


        dPeriod = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] == yearValue) & 
            (d['age'] <= 90),
            ['age', 'number_of_deaths']
        ]

        dCohort = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] - d['age'] == cohortValue) &
            (d['age'] <= 90),
            ['age', 'number_of_deaths']
        ]
        return dAge, dPeriod, dCohort
    elif typeValue == 'exposures':
        d = pd.read_csv("assets/data/exposures.csv")

        dAge = d.loc[
            (d['sex'] == sexValue) &
            (d['cntry'] == placeValue) & 
            (d['age'] == ageValue),
            ['year', 'exposures_count'] 
        ]

        dPeriod = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] == yearValue) & 
            (d['age'] <= 90),
            ['age', 'exposures_count']
        ]

        dCohort = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] - d['age'] == cohortValue) & 
            (d['age'] <= 90),
            ['age', 'exposures_count']
        ]
        return dAge, dPeriod, dCohort
    elif typeValue == 'Mx':
        d = pd.read_csv("assets/data/Mx.csv")
        dAge = d.loc[
            (d['sex'] == sexValue) &
            (d['cntry'] == placeValue) & 
            (d['age'] == ageValue),
            ['year', 'mx'] 
        ]

        dPeriod = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] == yearValue) & 
            (d['age'] <= 90),
            ['age', 'mx']
        ]

        dCohort = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] - d['age'] == cohortValue) & 
            (d['age'] <= 90),
            ['age', 'mx']
        ]
        return dAge, dPeriod, dCohort
    elif typeValue == 'population':
        d = pd.read_csv("assets/data/population.csv")
        dAge = d.loc[
            (d['sex'] == sexValue) &
            (d['cntry'] == placeValue) & 
            (d['age'] == ageValue),
            ['year', 'population_count'] 
        ]

        dPeriod = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] == yearValue) & 
            (d['age'] <= 90),
            ['age', 'population_count']
        ]

        dCohort = d.loc[
            (d['sex'] == sexValue) & 
            (d['cntry'] == placeValue) & 
            (d['year'] - d['age'] == cohortValue) & 
            (d['age'] <= 90),
            ['age', 'population_count']
        ]
        return dAge, dPeriod, dCohort
    elif typeValue == 'lifetables':
        d = pd.read_csv("assets/data/lifetables.csv")
        # Need to change total value of sex to both
        sexValueAdjusted = 'both' if sexValue == 'total' else sexValue

        dAge = d.loc[
            (d['sex'] == sexValueAdjusted) &
            (d['cntry'] == placeValue) & 
            (d['age'] == ageValue),
            ['year', 'ex'] 
        ]

        dPeriod = d.loc[
            (d['sex'] == sexValueAdjusted) & 
            (d['cntry'] == placeValue) & 
            (d['year'] == yearValue) & 
            (d['age'] <= 90),
            ['age', 'ex']
        ]

        dCohort = d.loc[
            (d['sex'] == sexValueAdjusted) & 
            (d['cntry'] == placeValue) & 
            (d['year'] - d['age'] == cohortValue) & 
            (d['age'] <= 90),
            ['age', 'ex']
        ]
        return dAge, dPeriod, dCohort

    return None
