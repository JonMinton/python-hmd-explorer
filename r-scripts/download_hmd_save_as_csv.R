# install.packages("tidyverse")
# install.packages('HMDHFDplus')
# install.packages('jsonlite')
# install.packages('glue')

# NOTE: To use from python consider adding the following to receive arguments 
# for usernames and passwords

args <- commandArgs(trailingOnly = TRUE)

username <- args[1]
password <- args[2]
# 
print("I'm in R")

print(paste("username:", username))
print(paste("password:", password))
library(tidyverse)
library(HMDHFDplus)
library(jsonlite)
library(glue)
library(janitor)

countryCodes <- HMDHFDplus::getHMDcountries()
countryCodes

# HMDHFDplus::getHMDitemavail(countryCodes$CNTRY[1])

# allHmdLinks <- countryCodes %>% 
#   mutate(
#     countryDataItems = map(CNTRY, HMDHFDplus::getHMDitemavail)
#   ) %>% 
#   unnest(cols = c(countryDataItems)) %>% 
#   rename(full_link = link1)

# # Let's test accessing a single item via full link

# # testFile <- HMDHFDplus::readHMDweb(pasteallHmdLinks$full_link[4])


if (!file.exists("assets/data/births.csv")){
  print("Cannot find births data. Downloading...")
  allBirths <- 
  countryCodes %>% 
  mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = 'Births', username=username, password=password)) %>% 
  unnest(dta) %>% 
  janitor::clean_names() %>% 
  pivot_longer(cols = female:total, names_to = "sex", values_to = "number_of_births")

  write_csv(allBirths, "assets/data/births.csv")
  print("Downloaded births data")
} else {
  print("Have already found deaths data. To force download delete the file in assets/data")
}

if (!file.exists("assets/data/deaths.csv")){
  print("Cannot find deaths data. Downloading...")
  allDeaths <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "Deaths_1x1", username=username, password=password)) %>% 
    unnest(dta) %>% 
    janitor::clean_names() %>% 
    select(-open_interval) %>% 
    pivot_longer(cols = female:total, names_to = "sex", values_to = "number_of_deaths")

  write_csv(allDeaths, "assets/data/deaths.csv")
  print("Downloaded deaths data")
} else {
  print("Have already found deaths data. To force download delete the file in assets/data")
}

if (!file.exists("assets/data/Mx.csv")){
  print("Can't find death rate data. Downloading")
  allMx <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "Mx_1x1", username = username, password = password)) %>%
    unnest(dta) %>% 
    janitor::clean_names() %>% 
    select(-open_interval) %>% 
    pivot_longer(cols = female:total, names_to = "sex", values_to = 'mx')

  write_csv(allMx, "assets/data/Mx.csv")
  print("Downloaded death rate data")
} else {
  print("Have already found death rate data. To force download delete the file in assets/data")
}

if (!file.exists("assets/data/population.csv")){
  print("Can't find population data. Downloading")
  allPopulation <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "Population", username=username, password=password)) %>% 
    unnest(dta) %>% 
    janitor::clean_names() %>% 
    mutate(female = (female1 + female2) /2, male = (male1 + male2) / 2, total = (total1 + total2 ) / 2 ) %>% 
    select(country, link, cntry, year, age, female, male, total) %>% 
    pivot_longer(cols = female:total, names_to = "sex", values_to = "population_count")

  write_csv(allPopulation, "assets/data/population.csv")
  print ("Downloaded population data")
} else {
  print("Have already found population data. To force download delete the file in assets/data")
}

if (!file.exists("assets/data/exposures.csv")){
  allExposures <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "Exposures_1x1", username=username, password=password)) %>% 
    unnest(dta) %>% 
    janitor::clean_names() %>% 
    select(country, link, cntry, year, age, female, male, total) %>% 
    pivot_longer(cols = female:total, names_to = "sex", values_to = "exposures_count")

  write_csv(allExposures, "assets/data/exposures.csv")
  print("Downloaded exposures data")
} else {
  print("Have already found exposures data. To force download delete the file in assets/data")
}

if (!file.exists("assets/data/lifetables.csv")){
  print("Downloading lifetables (n.b. this may take a while...)")
  femaleLifetables <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "fltper_1x1", username=username, password=password)) %>% 
    unnest(dta)
  names(femaleLifetables) <- c("country", "link", "cntry", "year", "age", "mx", "qx", "ax", "lx", "dx", "Lx", "Tx", "ex", "openinterval")

  femaleLifetables <- 
    femaleLifetables %>% 
      select(-openinterval) %>% 
      mutate(sex = 'female') %>% 
      select(country, link, cntry, sex, everything())

  femaleLifetables


  maleLifetables <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "mltper_1x1", username=username, password=password)) %>% 
    unnest(dta)
  names(maleLifetables) <- c("country", "link", "cntry", "year", "age", "mx", "qx", "ax", "lx", "dx", "Lx", "Tx", "ex", "openinterval")

  maleLifetables <- 
    maleLifetables %>% 
    select(-openinterval) %>% 
    mutate(sex = 'male') %>% 
    select(country, link, cntry, sex, everything())



  bothLifetables <- 
    countryCodes %>% 
    mutate(dta = map(CNTRY, HMDHFDplus::readHMDweb, item = "bltper_1x1", username=username, password=password)) %>% 
    unnest(dta)
  names(bothLifetables) <- c("country", "link", "cntry", "year", "age", "mx", "qx", "ax", "lx", "dx", "Lx", "Tx", "ex", "openinterval")

  bothLifetables <- 
    bothLifetables %>% 
      select(-openinterval) %>% 
      mutate(sex = 'both') %>% 
      select(country, link, cntry, sex, everything())


  allLifetables <- 
    bothLifetables %>% 
      bind_rows(
        femaleLifetables
      ) %>% 
      bind_rows(
        maleLifetables
      )


  write_csv(allLifetables, "assets/data/lifetables.csv")

} else {
  print("Already found lifetables.csv in assets/data. To force redownload delete from assets/data")
}




# allHmdDataOfInterest <- 
#   allHmdLinks %>% 
#     select(CNTRY, item)  %>% 
#     distinct() %>% 
#     filter(item %in% c(
#       "Births",
#       "Deaths_1x1",
#       "Population",
#       "Exposures_1x1",
#       "Mx_1x1",
#       "fltper_1x1",
#       "mltper_1x1",
#       "bltper_1x1",
#       "E0per",
#       "cExposures_1x1",
#       "cMx_1x1"
#     )) %>% 
#   mutate(
#     data = map2(CNTRY, item, HMDHFDplus::readHMDweb, username=username, password=password)
#   ) %>% 
#   unnest(data)



