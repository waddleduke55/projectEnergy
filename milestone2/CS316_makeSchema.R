library(readr)
library(dplyr)

power_database <- read_csv("Power_Database.csv")
acces_elec <- read_csv("access-electricity.csv")
filtered_main_db <- power_database %>%
  filter(`Indicator - Topic` == "Supply", `Country Name` != "Africa", grepl("generated", `Indicator Name`), `2018` != "0") %>%
  select(`Country Name`, `Main Grouping`, `Indicator - Unit`, `2018`)

filtered_main_db <- filtered_main_db %>%
  mutate(seller_email = paste("s", row_number(), "@gmail.com", sep = ""))

#make Members
Members <- filtered_main_db %>%
  select(seller_email)
Members <- Members %>%
  mutate(name = paste("s", row_number(), sep = ""))

names(Members) <- c("email", "name")

# Make Countris
acces_elec <- acces_elec %>%
  mutate(percent_pop_needs_elec = 100 - `Population-access-to-electricity-National-(%-of-population)`)
names(acces_elec) <- c("name", "pop_with_elec", "percent_pop_needs_elec")

Countries <- acces_elec %>%
  select(name, percent_pop_needs_elec)

# make Sellers

Sellers <- filtered_main_db %>%
  select(`Country Name`, seller_email, `2018`)
names(Sellers) <- c("country_name", "email", "total_produced_2018_Gwh")

Sellers <- Sellers %>%
  mutate(phone_number = (as.character(2027170000 + row_number()*101 + row_number())),
         address = paste(row_number(), "St", row_number()*100, sep = " "),
         total_produced_2018_Gwh = as.numeric(total_produced_2018_Gwh))

prices <- round(runif(248, 0.02, 0.06), 3)
Sellers$price_per_kwh <- prices

Sellers <- Sellers[c(2,4, 5, 1,3, 6)]

#create csvs
write.csv(Members, "Members.csv")
write.csv(Sellers, "Sellers.csv")
write.csv(Countries, "Countries.csv")