# options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)

username <- args[1]
password <- args[2]

print(args)
print(username)
print(password)

# install.packages("tidyverse", repos = "https://cran.r-project.org")
# install.packages("HMDHFDplus", repos = "https://cran.r-project.org")

# library(tidyverse)
library(HMDHFDplus)

hmdCountryCodes = getHMDcountries()


return(hmdCountryCodes)
# username <- "jon.will.minton@gmail.com"
# password <- "passphrase"

# hmd_dta <- data_frame(
#   code = getHMDcountries()
# ) %>% 
#   mutate(deaths = map(code, readHMDweb, item = "Deaths_1x1", username = username, password = password)) %>% 
#   mutate(population = map(code, readHMDweb, item = "Population", username = username, password = password)) %>% 
#   mutate(exposures = map(code, readHMDweb, item = "Exposures_1x1", username = username, password = password))

# hmd_dta %>% 
#   mutate(deaths = map(
#     deaths, 
#     function(x) {
#       x %>% 
#         select(-OpenInterval) %>% 
#         gather(Female:Total, key = "gender", value = "num_deaths")
#     }
#   )
#   ) %>% 
#   mutate(population = map(
#     population,
#     function(x) {
#       x %>% 
#         mutate(Female = ( Female1 + Female2 ) / 2) %>% 
#         mutate(Male = (Male1 + Male2) / 2) %>% 
#         mutate(Total = (Total1 + Total2) / 2) %>% 
#         select(Year, Age, Female, Male, Total) %>% 
#         gather(Female:Total, key = "gender", value = "num_population")
#     }
#   )
#   ) %>% 
#   mutate(exposures = map(
#     exposures,
#     function(x) {
#       x %>% 
#         select(-OpenInterval) %>% 
#         gather(Female:Total, key = "gender", value = "exposure")
#     }
#   )) %>% 
#   mutate(
#     dta_joined = pmap(
#       list(deaths, population, exposures), 
#       function(a, b, c) {
#         reduce(list(a, b, c), inner_join)
#       })
#   ) %>% 
#   select(code, dta_joined) %>% 
#   unnest() -> joined_data

# joined_data %>% write_csv("../assets/hmd_data.csv")