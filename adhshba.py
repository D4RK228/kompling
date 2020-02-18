```python
from fuzzywuzzy import fuzz
import pandas as pd

database = []
for i in pd.read_csv("greedy.csv")["text"]:
    database.append(i)
a =""
for i in database:
    i = i.split()
    for j in i:
        if len(j) > 2:
            a = j
            for k in range(len(database)):
                print(type(database[k]))
                n = database[k].split()
                for m in range(len(n)):
                    if fuzz.ratio(a, n[m]) >= 70:
                        n[m] = a
                database[k] = n

print(database)
```
