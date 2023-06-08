import json 

def generateTypeLookups():
    typeKv = [
        {"label" : "Births", "value" : "births"},
        {"label" : "Deaths", "value" : "deaths"},
        {"label" : "Exposures", "value" : "exposures"},
        {"label" : "Mortality Rates", "value" : "Mx"},
        {"label" : "Population Sizes", "value" : "population"}
    ]

    print("Started writing list of data types to a file")
    with open("../assets/lookups/places_by_type.json", "w") as fp:
        json.dump(typeKv, fp)  # encode dict into JSON
    print("Done writing list of data types  .json file")
