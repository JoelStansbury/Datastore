import json

'''Loads a JSON file into a python dictionary'''
def load(fname, args):
    with open(fname) as f:
        text = f.read()
        return json.loads(text)

'''
Saves input data as a JSON
Valid input data structures: dict, list, tuple, string, int, float, bool, None
'''
def save(data, fname, args):
    text = json.dumps(data)
    with open(fname, 'w') as f:
        f.write(text)

def help():
    print("JSON\n\tload(fname): Loads a JSON file into a python dictionary\n\tsave(data,fname): Saves input data as a JSON\n\t\tValid input data structures: dict, list, tuple, string, int, float, bool, None")
