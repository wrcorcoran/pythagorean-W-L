# unnecessary functions

teams = []

# function to calculate pythagorean win
def pyth(team, x):
    wins = round((team.runs_scored**(x) / (team.runs_scored**(x) + team.runs_allowed**(x))) * 162)

    return wins

class team:
    wins = 0
    losses = 0
    runs_allowed = 0
    runs_scored = 0

    def __init__(self, w, l, rs, ra):
        self.wins = w
        self.losses = l
        self.runs_allowed = ra
        self.runs_scored = rs

    def print(self):
        print("Wins: " + str(self.wins) + " / Losses: " + str(self.losses) + " --- Runs Scored: " +
              str(self.runs_scored) + " / Runs Allowed: " + str(self.runs_allowed))

# create list of team objects called train through 2014
train = []
for i in range(0, len(teams)):
    if (teams["year"][i] < 2015):
        train.append(team(teams["w"][i], teams["l"][i], teams["r"][i], teams["ra"][i]))

test = []
for i in range(0, len(teams)):
    if (teams["year"][i] == 2015):
        test.append(team(teams["w"][i], teams["l"][i], teams["r"][i], teams["ra"][i]))

print(float(len(train) / (len(train) + len(test))))