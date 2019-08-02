import pickle

'''Retrieves the data structure preserved in the pickle'''
def load(filename, args):
    with open(filename, 'rb') as f:
        return pickle.load(f)


'''
Saves input data as a pickle
Valid input data structures: ALL
'''
def save(data, filename, args):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def help():
    print('PKL reader/writer\n\tSaves and loads python data structures')
