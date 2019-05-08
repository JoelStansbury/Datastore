# Author: Joel Stansbury
# May 8, 2019
import json
import pickle



'''
Assigns a datatype to a given string
e.g. if a string can be parsed as an Int, parseUnknown will return that Integer

Empty strings ('') are parsed as None
'''
def parseUnknown(val):
    if val == '':
        return None
    datatypes = [int, float, str]
    for t in datatypes:
        try:
            return t(val)
        except: pass

'''Gets the file extension of a given filename (i.e. the string of characters after the last period)'''
def figure_out_structure(filename):
    return filename.split('.')[-1].lower()

'''
Loads a delimited file into a list of lists (i.e. column of rows)
'''
def load_delimited(filename, delimiter):
    data = []
    with open(filename) as f:
        text = f.read()
    lines = text.split('\n')
    for l in lines:
        row = l.split(delimiter)
        datum = []
        for d in row:
            datum.append(parseUnknown(d))
        data.append(datum)
    return data

def load_tsv(filename, args):
    return load_delimited(filename, delimiter='\t')

def load_csv(filename, args):
    return load_delimited(filename, delimiter=',')


'''Loads a JSON file into a python dictionary'''
def load_json(filename, args):
    with open(filename) as f:
        text = f.read()
        return json.loads(text)

'''Retrieves the data structure preserved in the pickle'''
def load_pickle(filename, args):
    with open(filename, 'rb') as f:
        return pickle.load(f)


'''Attempts to load a file using a generic approach based on the file extension'''
loaders = {"csv":load_csv,"tsv":load_tsv,'json':load_json,'pkl':load_pickle}
def load(filename, datastruct = None, args = {}):
    if datastruct == None:
        datastruct = figure_out_structure(filename)
    return loaders[datastruct](filename, args)




'''
Saves input data as a delimited file, e.g. csv or tsv
Valid input data structures: dict, Iterable
'''
def save_delimited(data, filename, args, delimiter):
    def list_to_row(l):
        t = ''
        for i in l:
            t = t+str(i)+delimiter
        t = t[:-1]+'\n'
        return t
    text = ''
    if type(data) == dict:
        headers = list(data.keys())
        text = text+list_to_row(headers)
        for i in range(len(data[headers[0]])):
            row = []
            for h in headers:
                row.append(data[h][i])
            text = text+list_to_row(row)
    else:
        text = ''
        for row in data:
            text = text+list_to_row(row)

    with open(filename,'w') as f:
        f.write(text[:-1])

def save_csv(data, filename, args):
    save_delimited(data, filename, args, ',')

def save_tsv(data, filename, args):
    save_delimited(data, filename, args, '\t')


'''
Saves input data as a JSON
Valid input data structures: dict, list, tuple, string, int, float, bool, None
'''
def save_json(data, filename, args):
    text = json.dumps(data)
    with open(filename, 'w') as f:
        f.write(text)

'''
Saves input data as a pickle
Valid input data structures: ALL
'''
def save_pickle(data, filename, args):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


'''
Attempts to save input data in the format indicated by the extension on filename
'''
savers = {"csv":save_csv, 'tsv':save_tsv, 'json':save_json, 'pkl':save_pickle}
def save(data, filename, args = {}):
    saver = savers[figure_out_structure(filename)]
    saver(data, filename, args)
