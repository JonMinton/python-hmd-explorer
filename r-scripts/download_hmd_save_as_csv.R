# install.packages("tidyverse")
# install.packages('HMDHFDplus')
# install.packages('jsonlite')
# install.packages('glue')

# NOTE: To use from python consider adding the following to receive arguments 
# for usernames and passwords

# args <- commandArgs(trailingOnly = TRUE)

# username <- args[1]
# password <- args[2]

library(tidyverse)
library(HMDHFDplus)
library(jsonlite)
library(glue)

countryCodes <- HMDHFDplus::getHMDcountries()
countryCodes

HMDHFDplus::getHMDitemavail(countryCodes$CNTRY[1])

allHmdLinks <- countryCodes %>% 
  mutate(
    countryDataItems = map(CNTRY, HMDHFDplus::getHMDitemavail)
  ) %>% 
  unnest(cols = c(countryDataItems)) %>% 
  rename(full_link = link1)

# Let's test accessing a single item via full link

# testFile <- HMDHFDplus::readHMDweb(pasteallHmdLinks$full_link[4])


allHmdDataOfInterest <- 
  allHmdLinks %>% 
    select(CNTRY, item)  %>% 
    distinct() %>% 
    filter(item %in% c(
      "Births",
      "Deaths_1x1",
      "Population",
      "Exposures_1x1",
      "Mx_1x1",
      "fltper_1x1",
      "mltper_1x1",
      "bltper_1x1",
      "E0per",
      "cExposures_1x1",
      "cMx_1x1"
    )) %>% 
  mutate(
    data = map2(CNTRY, item, HMDHFDplus::readHMDweb, username=username, password=password)
  ) %>% 
  unnest(data)



