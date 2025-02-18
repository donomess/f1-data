import pandas as pd
import wins
import podiums

#Load in data
circuits = pd.read_csv("f1-data/csv data/circuits.csv")
constructor_results = pd.read_csv("f1-data/csv data/constructor_results.csv")
constructor_standings = pd.read_csv("f1-data/csv data/constructor_standings.csv")
constructors = pd.read_csv("f1-data/csv data/constructors.csv")
driver_standings = pd.read_csv("f1-data/csv data/driver_standings.csv")
drivers = pd.read_csv("f1-data/csv data/drivers.csv")
lap_times = pd.read_csv("f1-data/csv data/lap_times.csv")
pit_stops = pd.read_csv("f1-data/csv data/pit_stops.csv")
qualifying = pd.read_csv("f1-data/csv data/qualifying.csv")
races = pd.read_csv("f1-data/csv data/races.csv")
results = pd.read_csv("f1-data/csv data/results.csv")
seasons = pd.read_csv("f1-data/csv data/seasons.csv")
sprint_results = pd.read_csv("f1-data/csv data/sprint_results.csv")
status = pd.read_csv("f1-data/csv data/status.csv")

#Merge data where applicable
gp_merge = results.merge(drivers, on="driverId")
sprint_merge = sprint_results.merge(drivers, on="driverId")

#Display GP wins & Sprint wins
wins.displayGPWins(gp_merge)
wins.displaySprintWins(sprint_merge)

#Display GP podiums & Sprint Podiums
podiums.displayGPPodiums(gp_merge)
podiums.displaySprintPodiums(sprint_merge)