import subprocess
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


# Next steps

# Check data file exists (about 380mb)
# If it does not run r-scripts/download_hmd_save_as_csv.R 
# from here passing hmd_user and hmd_pass 
# as arguments in subprocess.call


subprocess.call(f"Rscript /Users/JonMinton/repos/python-hmd-explorer/r-scripts/download_hmd_save_as_csv.R {hmd_user} {hmd_pass}", shell = True)
