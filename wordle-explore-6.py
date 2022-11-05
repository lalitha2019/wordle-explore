#############
#Objective: To become comfortable with Python syntax, 
# and to have some fun
#Task chosen: To explore patterns of letter placing in wordle
#Data: List of word I solved in last 70 days or so, 
#Missed noting a couple of them. So, there are 66 words
#Known bug: Letters in first place are not being counted
#This is because when I saved words they all started with #Capital letter.
#Unknowns: There could be mistakes as I tested quickly and not exhaustively
#Improvement goals: tidying up, adding a few summary explorations from earlier versions
#Enhancement goals: to capture additions and explore possibilites of predictions
#Time taken: 6 to 8 hours today over a period of 2 days (3rd and 4th Nov. 2022)
############

#Learning point 1: how to add the value_counts as additional column
#Learning point 2: how to write dataframe to a file
#Learning point 3: how to generate a list of letters within a range
#Learning point 4: How to get a single cell from dataframe
#learning point 5: use unique!!! if letter in df[column].unique() #nom values in a olcumn is > 26. So, without unique, letter index will go out of range.
#Learning point 6: how to access counts of a particular value in a given column: df[column].value_counts()[letter]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read the words from file
with open("wordle-words.txt", "r") as wordle_file:
	words = wordle_file.readlines()

columnList = ['L1', 'L2', 'L3', 'L4', 'L5']

#letters would contain a list of lists.
#each list in letters is a list of letters for a word from words.
letters = []
a = range(5)
j = 0

for word in words:
 tmp = []
 for i in a:
  tmp.insert(i,word[i])
 letters.append(tmp)
 j +=1

#convert list to dataframe and add a header.
df = pd.DataFrame(letters, columns=columnList)

#Learning point 1: how to add the value_counts as additional column
for column in columnList:
    b = 'freq' + column
    df[b] = df.groupby(column)[column].transform('count')

#Learning point 2: how to write dataframe to a file
with open("wordle-df.txt",'w') as outfile:
    df.to_string(outfile)

#Learning point 3: how to generate a list of letters within a range
letterRange = range(ord('a'),ord('z')+1)
letterList = []
for num in letterRange:
    letterList.append(chr(num))
print(letterList)

#Learning point 4: How to get a single cell from dataframe
val = df.loc[df.L4=='a', 'freqL2'].values[0]
#print(val)

#learning point 5: use unique!!! if letter in df[column].unique()
#num of values in a olcumn is > 26. So, without unique, letter index will go out of range.
#Learning point 6: how to access counts of a particular value in a given column: df[column].value_counts()[letter]
rows = []
for column in columnList:
    tmp = []
    i = 0
    index = 0
    for letter in letterList:
        if letter in df[column].unique():
            tmp.insert(i,df[column].value_counts()[letter])
            index += 1
        else:
            tmp.insert(i,0)
        i = i + 1
    rows.append(tmp)
df1 = pd.DataFrame(rows,columns=letterList)
df2 = df1.transpose()
df2.plot.bar(rot=0)
plt.show()

