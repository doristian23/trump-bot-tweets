import pandas as pd
import re

question = re.compile(r'\?') # question regex object
trmp = re.compile(r'\bTrump\b') # trump regex object

df1 = pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\School\COMP 598\IRAhandle_tweets_1.csv")
df10k = df1.iloc[0:10000]  # first 10000 twts
dfeng = df10k[df10k['language'] == 'English'] # keeping english twts


def findq(tweet): # function that looks for questions
    q = re.search(question, tweet)
    if q is None:
        return 0
    else:
        return 1


q_s = []
for i, x in dfeng.iterrows(): # looking for question twts
    q_s.append(findq(x[2]))

dfeng.insert(3, 'qs', q_s)
dfnoq = dfeng[dfeng['qs'] == 0] # keeping non-question twts
dfnoq = dfnoq.drop(columns=['qs']) # dropping question feature column
dfnoq.to_csv("prelim_dataset.tsv", sep="\t")


def findTrump(tweet): # function that looks for Trump tweets
    t = re.search(trmp, tweet)
    if t is None:
        return False
    else:
        return True


trumpM = []
for i, x in dfnoq.iterrows(): # looking for trump twts
    trumpM.append(findTrump(x[2]))

dfnoq.insert(3, 'trump_mention', trumpM) # inserting trump feature col
dfTrump = dfnoq.iloc[0:, 0:4] # dropping all other cols
dfTrump.to_csv("dataset.tsv", sep="\t")
