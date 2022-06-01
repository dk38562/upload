import pandas as pd

df = pd.read_csv('Wordle answers.csv')
df.set_index("Date", inplace=True)
answer = df.iloc[03/23/2022]
print(answer)
