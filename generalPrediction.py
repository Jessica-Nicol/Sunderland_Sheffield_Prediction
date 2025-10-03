import csv

# GENERAL OUTCOME
print ('Prediction For General Outcome Based On Performance Of All Games Played Across The Season')

def loadMatches(fileName, teamName):
    matches = []
    with open('cleanData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Team'] == teamName:
                matches.append(row['Outcome'])
    return matches

sunderlandOutcome = loadMatches('cleanData.csv', 'Sunderland')
sheffieldOutcome = loadMatches('cleanData.csv', 'Sheffield United')

def outcomeStats(Outcome):
    total = len(Outcome)
    winPercentage = (Outcome.count('W')/total)*100
    lossPercentage = (Outcome.count('L')/total)*100
    drawPercentage = (Outcome.count('D')/total)*100
    return winPercentage, lossPercentage, drawPercentage
sunW, sunL, sunD = outcomeStats(sunderlandOutcome)
sheW, sheL, sheD = outcomeStats(sheffieldOutcome)

print (f"Sunderland:\nW: {sunW:.2f}\nL: {sunL:.2f}\nD: {sunD:.2f}")
print (f"Sheffield United:\nW: {sheW:.2f}\nL: {sheL:.2f}\nD: {sheD:.2f}")

def predictOutcome(sunW, sunL, sunD, sheW, sheL, sheD):
    winScore = (sunW + sheL)/2
    lossScore = (sunL + sheW)/2
    drawScore = (sunD + sheD)/2

    if winScore > max(lossScore, drawScore):
        return "Predicted Outcome: Sunderland to Win"
    elif lossScore > max(winScore, drawScore):
        return "Predicted Outcome: Sheffield United to Win"
    else:
        return "Predicted Outcome: Draw"

print (predictOutcome(sunW, sunL, sunD, sheW, sheL, sheD))

# H2H EXACT SCORE
h2h = []
print ('Analysis Using H2H Games Played')
print ('List of H2H Games:')
with open('cleanData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Team'] == 'Sunderland' and row['Opponent'] == 'Sheffield United':
            sunderlandGoals = int(row['GoalsFor'])
            sheffieldGoals = int(row['GoalsAgainst'])
            print('Sunderland ', sunderlandGoals, ' - Sheffield United ', sheffieldGoals)
            h2h.append((sunderlandGoals, sheffieldGoals))

avgSheffield = sum(m[1] for m in h2h) / len(h2h)
avgSunderland = sum(m[0] for m in h2h) / len(h2h)
print ('Predicted H2H Score: Sunderland ', round(avgSunderland), ' - Sheffield United ', round(avgSheffield))