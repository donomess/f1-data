import matplotlib.pyplot as plt

#Caluclate & Display Podiums by Driver
def displayGPPodiums(data):
    #Refine data to get podiums
    gp_podiums = data[data["positionOrder"] <= 3].groupby("surname")["positionOrder"].count().reset_index()
    gp_podiums.columns = ["Driver", "Podiums"]
    gp_podiums = gp_podiums.sort_values(by="Podiums", ascending=False)

    #Display in output
    print("Top 25 drivers by GP Podium Finishes--")
    print(gp_podiums.head(25).to_string(index=False))

def displaySprintPodiums(data):
    #Refine data to get podiums
    sprint_podiums = data[data["positionOrder"] <= 3].groupby("surname")["positionOrder"].count().reset_index()
    sprint_podiums.columns = ["Driver", "Podiums"]
    sprint_podiums = sprint_podiums.sort_values(by="Podiums", ascending=False)

    #Display in output
    print("Top 5 drivers by Sprint Podium Finishes--")
    print(sprint_podiums.head(5).to_string(index=False))
