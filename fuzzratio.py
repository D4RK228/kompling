from fuzzywuzzy import fuzz
import pandas as pd

database = []
for i in pd.read_csv("greedy.csv")["text"]:
    database.append(i)
    
for i in range(len(database)):
    database[i] = database[i].split()
    for j in range(len(database[i])):
        database[i][j] = database[i][j].split() #####  Чистим от знаков препинания
        for k in database[i][j]:
            temp = ""
            for k in str(database[i][j][0]):
                if ord(k) >= 1040 and ord(k) <= 1105:
                    temp += k
                database[i][j] = str(temp)
a =""
for i in database:
    for j in i:
        if len(j) > 2:
            a = j
            for k in range(len(database)):   
                n = database[k]
                for m in range(len(n)):
                    if fuzz.ratio(a, n[m]) >= 70: ####  МЕНЯЕМ СЛОВА ПО FUZZ.RATIO()
                        n[m] = a
                database[k] = str(n)
                print(database[k])

print(database)
