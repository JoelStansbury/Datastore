# Datastore
Python module which loads and saves data structures based on the file extension

Why can't python be more like my OS. I never have to explain how to read through a csv to windows. What? There are too many variables to consider? No says I. This module attempts to follow a generic procedure for reading and writing common data storage formats using only the file extension for guidance. If that fails, then yes, you probably should take the time to do it the right way. 

Currently supported file structures: CSV TSV JSON PICKLE 

(please let me know if you'd like to add more to this list)

```
import Datastore

d = {'id': [1,2,3,4],'otherID':[4,3,2,1]}


# save this dict as a pickle
Datastore.save(d, 'test.pkl')

# open it back up as a dict
d = Datastore.load('test.pkl')

# save it again as a JSON
Datastore.save(d, 'test.json')

# open it back up as a dict
d = Datastore.load('test.json')

# this time save it as a tsv (will not go back to a dict on its own because some tsv's don't have headers)
Datastore.save(d, 'test.tsv')

# open it back up as a list of lists
d = Datastore.load('test.tsv')

# save the list of lists as a pickle again
Datastore.save(d, 'test.pkl')

# open it back up
d = Datastore.load('test.pkl')

# save it as a csv
Datastore.save(d, 'test.csv')

# open it back up
d = Datastore.load('test.csv')

# print out the result
print(d)
```
