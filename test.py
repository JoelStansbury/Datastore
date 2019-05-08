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

# this time save it as a tsv (cannot go back to a dict)
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
