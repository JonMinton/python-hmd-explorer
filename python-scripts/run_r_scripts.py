# OS for environment variables (to avoid saving on github)
import os
# pandas for python data science
import pandas as pd

# r2py imports 
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr
from dotenv import load_dotenv

# Get environment variables
load_dotenv()

hmd_user = os.environ.get('HMD_USERNAME')
hmd_pass = os.environ.get('HMD_PASSWORD')

# Install specific R package (to use via python)
hmdHfdPlus = importr('HMDHFDplus')
# tv = importr('tidyverse')

# print(f'hmd_user is {hmd_user}')
# print(f'hmd_pass is {hmd_pass}')

# Run R package, returning R dataframe
eligibleCountries = hmdHfdPlus.getHMDcountries()

print(eligibleCountries)
print(type(eligibleCountries))




# convert R dataframe to pd equivalent
with (ro.default_converter + pandas2ri.converter).context():
  eligibleCountriesPd = ro.conversion.get_conversion().rpy2py(eligibleCountries)

print(eligibleCountriesPd)
print(type(eligibleCountriesPd))

# What are the types of data that are avaialbel for a particular country
# indicated by country code, e.g. FIN (Finland)?

availItems = hmdHfdPlus.getHMDitemavail('FIN')

print(availItems)

pd.DataFrame(availItems).transpose().to_csv('availItems.csv', index = False)
