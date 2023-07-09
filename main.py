import pandas as pd
from sklearn.metrics import r2_score
import numpy as np


# parse csv file
teams = pd.read_csv("team.csv")

# restrict to seasons between 1962 and 2015
teams = teams[teams["year"] >= 1962]
teams = teams[teams["year"] <= 2015]
teams = teams[teams["g"] == 162]
teams = teams[["year", "w", "l", "r", "ra"]]
teams = teams.reset_index(drop=True)

train_teams = teams[teams["year"] <= 2014]
test_teams = teams[teams["year"] == 2015]

best_x = None
best_r2 = -float('inf')

pd.options.mode.chained_assignment = None

for x in np.arange(1.0001, 10.0001, 0.0001):
    train_teams.loc[:, 'result'] = round((train_teams['r'] ** x) / (train_teams['r'] ** x + train_teams['ra'] ** x) * 162)

    r2 = r2_score(train_teams['w'], train_teams['result'])

    if r2 > best_r2:
        best_r2 = r2
        best_x = x

# best_x = 1.8391

print("Best value for x:", str(round(best_x, 4)))
print("Best R-squared:", str(round(best_r2, 10)))

test_teams['result'] = round((test_teams['r'] ** best_x) / (test_teams['r'] ** best_x + test_teams['ra'] ** best_x) * 162)

print("Predicted wins for 2015:")
print(test_teams[['w', 'result']])