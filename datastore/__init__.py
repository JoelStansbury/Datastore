import importlib
import os

filetypes = {}
cwd = os.getcwd()
dirname = os.path.dirname(__file__)

os.chdir(dirname)
addons = os.listdir('extensions/')
for fname in addons:
    if fname == '__pycache__':
        pass
    else:
        filetypes[fname] = importlib.import_module('.' + fname,'extensions')
os.chdir(cwd)

def load(fname, args = {}):
    ext = fname.split('.')[-1].lower()
    return filetypes[ext].load(fname, args)

def save(data, fname, args = {}):
    ext = fname.split('.')[-1].lower()
    return filetypes[ext].save(data, fname, args)

def help(ext):
    filetypes[ext].help()
