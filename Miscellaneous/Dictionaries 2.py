def football():

    teams = {"Everton": {"Wins" : 78, "Losses" : 0 }, "Liverpool": {"Wins" : 0, "Losses" : 110 }, "Man City": {"Wins" : 20, "Losses" : 2 }}

    for keys, **values in teams.items():
            print(keys, Wins, Losses )

football()