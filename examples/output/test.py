import datastore
import os

d = [{'id': [1,2,3,4],'otherID':[4,3,2,1]}]


# save this dict as a pickle
datastore.save(d, 'test.pkl')

# open it back up as a dict
d = datastore.load('test.pkl')

# save it again as a JSON
datastore.save(d, 'test.json')

# open it back up as a dict
d = datastore.load('test.json')


# save the list of lists as a pickle again
datastore.save(d, 'test.pkl')

# open it back up
d = datastore.load('test.pkl')

# save it as a csv
datastore.save(d, 'test.csv')

# open it back up
d = datastore.load('test.csv')

# print out the result
print(d)
