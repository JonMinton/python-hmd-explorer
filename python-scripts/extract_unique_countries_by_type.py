import json
import pandas as pd

def extractUniqueCountriesByType():
    locs = [
        {"type" : "births", "loc" : "../assets/data/births.csv"},
        {"type" : "deaths", "loc" : "../assets/data/deaths.csv"},
        {"type" : "exposures", "loc" : "../assets/data/exposures.csv"},
        {"type" : "lifetables", "loc" : "../assets/data/lifetables.csv"},
        {"type" : "Mx", "loc" : "../assets/data/Mx.csv"},
        {"type" : "population", "loc" : "../assets/data/population.csv"}
    ]

    def makeKv(loc):
        return [
        {"label" : x['country'], "value" : x['cntry']}
            for i, x in 
                pd.read_csv(loc)[
                    ['country', 'cntry']
                ].drop_duplicates(
                ).iterrows()          
        ]

    jsonKv = {x['type'] : makeKv(x['loc'])  for x in locs}
    # Using a dict comprehension not a list comprehension! 
    # jsonKv

    print("Started writing dictionary to a file")
    with open("../assets/lookups/places_by_type.json", "w") as fp:
        json.dump(jsonKv, fp)  # encode dict into JSON
    print("Done writing dict into .json file")