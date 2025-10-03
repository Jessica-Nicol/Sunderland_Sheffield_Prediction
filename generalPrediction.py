import csv

def load_matches(fileName, teamName):
    matches = []
    with open(fileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Team'] == teamName:
                matches.append({
                    'goalsFor': int(row['GoalsFor']),
                    'goalsAgainst': int(row['GoalsAgainst']),
                    'opponent': (row['Opponent']),
                    'home': (row['Home']),
                    'outcome': (row['Outcome']),
                })
    return matches

sunderlandMatches = load_matches('cleanData.csv', 'Sunderland')
sheffieldMatches = load_matches('cleanData.csv', 'Sheffield United')

# GENERAL OUTCOME
print ('Prediction For General Outcome Based On Performance Of All Games Played Across The Season')

sunW = 0
sunD = 0
sunL = 0
sheW = 0
sheD = 0
sheL = 0
with open('cleanData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if ((row['Team'] == 'Sunderland') and (row['Outcome'] == 'W')):
            sunW = sunW+1
        elif ((row['Team'] == 'Sunderland') and (row['Outcome'] == 'D')):
            sunD = sunD+1
        elif ((row['Team'] == 'Sunderland') and (row['Outcome'] == 'L')):
            sunL = sunL+1
        elif ((row['Team'] == 'Sheffield United') and (row['Outcome'] == 'W')):
            sheW = sheW+1
        elif ((row['Team'] == 'Sheffield United') and (row['Outcome'] == 'D')):
            sheD = sheD+1
        elif ((row['Team'] == 'Sheffield United') and (row['Outcome'] == 'L')):
            sheL = sheL+1

if ((((sunW/len(sunderlandMatches))*100) + ((sheL/len(sheffieldMatches))*100)) > (((sheW/len(sheffieldMatches))*100)) + ((sunL/len(sunderlandMatches))*100)):
    print("Sunderland more likely to win")
elif ((((sunL / len(sunderlandMatches)) * 100) + ((sheW / len(sheffieldMatches)) * 100)) > (((sheL / len(sheffieldMatches)) * 100)) + ((sunW / len(sunderlandMatches)) * 100)):
    print("Sheffield United more likely to win")
else:
    print("Both teams had the same win percentage")
