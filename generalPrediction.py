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
