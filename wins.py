import matplotlib.pyplot as plt

#Calculate & Display wins per driver
def displayGPWins(data):
    #Refine data just to obtain driver wins
    gp_wins = data[data["positionOrder"] == 1].groupby("surname")["positionOrder"].count().reset_index()
    gp_wins.columns = ["Driver", "Wins"]
    gp_wins = gp_wins.sort_values(by="Wins", ascending=False)

    #Make data plot to display data
    plt.figure(figsize=(12,6))
    plt.barh(gp_wins["Driver"].head(25)[::-1], gp_wins["Wins"].head(25)[::-1], color='blue')
    plt.xlabel("Number of Grand Prix Wins")
    plt.ylabel("Driver Name")
    plt.title("25 most winningest F1 drivers of all time, GP")
    plt.grid(axis='x', linestyle='--', alpha=0.8)
    plt.show()

def displaySprintWins(data):
    #Refine to just sprint wins
    sprint_wins = data[data["positionOrder"] == 1].groupby("surname")["positionOrder"].count().reset_index()
    sprint_wins.columns = ["Driver", "Wins"]
    sprint_wins = sprint_wins.sort_values(by="Wins", ascending=False)

    #Display on a plot
    plt.figure(figsize=(12,6))
    plt.barh(sprint_wins["Driver"].head(5)[::-1], sprint_wins["Wins"].head(5)[::-1], color='blue')
    plt.xlabel("Number of Sprint Wins")
    plt.ylabel("Driver Name")
    plt.title("5 most winningest F1 drivers of all time, Sprint")
    plt.grid(axis='x', linestyle='--', alpha=0.8)
    plt.show()