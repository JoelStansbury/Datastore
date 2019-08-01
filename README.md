# Datastore
### Currently supported file structures: CSV TSV JSON PICKLE 
Python module which loads and saves data structures based on the file extension


Why can't python be more like my OS. I never have to explain how to read through a csv to windows. What? There are too many variables to consider? No says I. This module attempts to follow a **generic procedure for reading and writing common data storage formats using only the file extension for guidance**. If that fails, then yes, you probably should take the time to do it the right way.

### Objective
The motivation here is as follows; Most of the time, the most generic approach to opening a file will work. It's usually not the fastest way, but if speed is not a bottleneck for you, you might as well spend your time manipulating the data as opposed figuring out how to load it into python. The goal of Datastore is to make implementing these generic approaches as fast as possible. If it doesn't work, well at least you didn't waste much time. Otherwise, you just skipped a monotonous task and can get on with real work.



### Usage
```
datastore.save(data, filename)
data = datastore.load(filename)
```


### Example
This is obviously not a normal use case, but it shows that the procedures for opening these file structures are identical, which is a nice change in my opinion.

```
import datastore

d = {'id': [1,2,3,4],'otherID':[4,3,2,1]}
```

save this dict as a pickle
```
datastore.save(d, 'test.pkl')
```
open it back up as a dict
```
d = datastore.load('test.pkl')
```
save it again as a JSON
```
datastore.save(d, 'test.json')
```
open it back up as a dict
```
d = datastore.load('test.json')
```
this time save it as a tsv. Currently the default structure when opening csv's and tsv's is a list of lists. Though I plan to add functionality to detect a header by comparing the data types of the first row with the subsequent rows. If a header is detected, then the csv will be opened as a dict. This is a WIP though
```
datastore.save(d, 'test.tsv')
  ```
open it back up as a list of lists
```
d = datastore.load('test.tsv')
```
save the list of lists as a pickle again
```
datastore.save(d, 'test.pkl')
```
open it back up
```
d = datastore.load('test.pkl')
```
save it as a csv
```
datastore.save(d, 'test.csv')
```
open it back up
```
d = datastore.load('test.csv')
```
print out the result
```
print(d)
```
