# Datastore
### Currently supported file structures: CSV WAV JSON PICKLE 
Python module which loads and saves data structures based on the file extension. 

### Dependencies
* Python3 (and native libraries)
  * json
  * csv
  * wave
  * struct
  * importlib
  * os
  * pickle


### Installation
`pip install loadsave`

### Usage

```
import loadsave

data = loadsave.load(filename)
... manipulating data ...
loadsave.save(data, filename)

```
Saving data can be a bit unintuitive. 
* `csv` requires data to be a list of dictionaries
* `wav` requires data to be a tuple or list of the form `(y,sr)` exactly how it would be returned by `load('example.wav')`



### Objective
This module attempts to follow a **generic procedure for reading and writing common data storage formats using only the file extension for guidance**.

The motivation here is as follows; Most of the time, the most generic approach to opening a file will work. It's may not be the most computationaly efficient way, but if loading time is not a bottleneck for your workflow, you might as well spend your time manipulating the data as opposed figuring out how to load it into python. The goal of Datastore is to make implementing these generic approaches as fast as possible. If it doesn't work, well at least you didn't waste much time. Otherwise, you just skipped a monotonous task and can get on with real work.




### Example
```
import loadsave

d = [{'id': [1,2,3,4],'otherID':[4,3,2,1]}]

# save this dict as a pickle
loadsave.save(d, 'test.pkl')
```
`'test.pkl'` can be replaced with `'test.json'`, or `'test.csv'`. Attempting to save it to `'test.wav'` will return an error, because `d` is not an acceptable format for an audio waveform.

However, if `d = [0,1,2,3,4]` you could call `loadsave.save((d,44100),'test.wav')`. `csv`s require a list of dictionaries, so trying to save _this_ as a csv will fail




### File Types
#### CSV
* This is just a wrapper for csv.DictReader() / csv.DictWritter()
* The data must be a list of dictionaries
#### WAV
* Restricted to 16-bit audio
* Can handle stereo/multi-channel waveforms
* Data must be a list or tuple of the form (waveform, samplerate), just like it is provided from `loadsave.load('example.wav')`
#### PICKLE
* This should work with any data structure in python.
#### JSON
* Can hanle `dict`, `list`, `str`, `int`, `float`, `bool`, and `None`
