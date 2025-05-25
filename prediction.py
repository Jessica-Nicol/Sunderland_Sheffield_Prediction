import pandas as pd

df = pd.read_csv('cleanData.csv')
df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

df = df.sort_values(by=['Team', 'Date'])
df['GF_Roll_5'] = df.groupby('Team')['GoalsFor'].rolling(5).mean().reset_index(level=0, drop=True)
df['GA_Roll_5'] = df.groupby('Team')['GoalsAgainst'].rolling(5).mean().reset_index(level=0, drop=True)
df.to_csv("averages.csv", index=False)
