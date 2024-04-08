import pandas as pd
import random 
import numpy as np 

df = pd.read_csv('Codewars Data.csv')
df['score'] = 0
df['TB1'] = 0
df['TB2'] = 0
df['matchplayed'] = ''
lang = df['Language of Code'] == 'P'
pydata = df[lang]
cppdata = df[~lang]  
pydatanew = pydata.sort_values(by= ['score','Initial Rting'], ascending=False, ignore_index=True)
cppdatanew = cppdata.sort_values(by= ['score','Initial Rting'], ascending=False, ignore_index=True)



def sort(df):
    sorted = df.sort_values(by= ['score','Initial Rting'], ascending=False)
    return sorted

def prob(r1, r2):
    diff = abs(r1 - r2)
    if diff > 10:
        return 0.1 if r2 > r1 else 0.9
    elif diff >= 5:
        return 0.35 if r2 > r1 else 0.65
    else:
        return 0.5 

def match(r1,r2):
    #noise = random.randint(-4,4)
    #rating of r1 and r2 used in match
    r1 = r1 + random.randint(-4,4)
    r2 = r2 + random.randint(-4,4)
    r1p = prob(r1,r2)
    r2p = 1.0 - r1p
    win = np.random.choice([1,0], p=[r1p,r2p])
    return win

def pairing(df):
    players = len(df)
    if players % 2 != 0:
        df.loc[players - 1,'score'] += 1
        df.loc[players - 1,'matchplayed'] += 'Bye'
        players = players - 1
    half = int(players/2)

    for i in range(half):
        r1 = df.loc[i,'Initial Rting']
        r2 = df.loc[i + half,'Initial Rting']

        #matches = pd.DataFrame(columns= ['matches'])
        #matches = matches._append(df.loc[i,'Team Name'] + df.loc[i + half,'Team Name'])
        win = match(r1, r2)

        #updating the results
        df.loc[i,'matchplayed'] += df.loc[i + half,'Team Name']
        df.loc[i + half,'matchplayed'] += df.loc[i,'Team Name']
        if win == 1:
            df.loc[i,'score'] += 1
            if r1 > r2:
                df.loc[i,'Initial Rting'] += 2
                df.loc[i + half,'Initial Rting'] -= 2
            else:
                df.loc[i,'Initial Rting'] += 5
                df.loc[i + half,'Initial Rting'] -= 5
        else:
            df.loc[i + half,'score'] += 1
            if r1 > r2:
                df.loc[i,'Initial Rting'] -= 5
                df.loc[i + half,'Initial Rting'] += 5
            else:
                df.loc[i,'Initial Rting'] -= 2
                df.loc[i + half,'Initial Rting'] += 2

    #print(matches)
    return df
        

#print(pydatanew)
print(pairing(pydatanew))
print(pydatanew.loc[0,'Initial Rting'])
#print(matches)

#rting above 100
#tiebreaks
#rting below 50
#pairings


