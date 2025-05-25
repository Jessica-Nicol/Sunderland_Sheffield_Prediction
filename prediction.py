import pandas as pd
from scipy.stats import poisson

df = pd.read_csv('cleanData.csv')
df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

df = df.sort_values(by=['Team', 'Date'])
df['GF_Roll_5'] = df.groupby('Team')['GoalsFor'].rolling(5).mean().reset_index(level=0, drop=True)
df['GA_Roll_5'] = df.groupby('Team')['GoalsAgainst'].rolling(5).mean().reset_index(level=0, drop=True)
df.to_csv("averages.csv", index=False)

df = pd.read_csv("averages.csv")
sunderland = df[df['Team'] == 'Sunderland'].sort_values(by='Date').iloc[-1]
sheffield = df[df['Team'] == 'Sheffield United'].sort_values(by='Date').iloc[-1]

sunderland_xG = (sunderland['GF_Roll_5']) + (sheffield['GA_Roll_5']) / 2
sheffield_xG = (sheffield['GF_Roll_5']) + (sunderland['GA_Roll_5']) / 2

print(f"Sunderland expected goals: {sunderland_xG:.2f}")
print(f"Sheffield Utd expected goals: {sheffield_xG:.2f}")