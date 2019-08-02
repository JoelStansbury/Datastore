import importlib.util
import os

filetypes = {}
cwd = os.getcwd()
dirname = os.path.dirname(__file__)
print("dirname:",dirname)


addons_dir = os.path.join(dirname,'extensions')
print("addons:",addons_dir)


addons = os.listdir(addons_dir)
for fname in addons:
    if fname == '__pycache__':
        pass
    else:
        p = os.path.normpath(os.path.join(addons_dir,fname+'/__init__.py'))
        spec = importlib.util.spec_from_file_location(fname, p)
        filetypes[fname] = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(filetypes[fname])


def load(fname, args = {}):
    ext = fname.split('.')[-1].lower()
    return filetypes[ext].load(fname, args)

def save(data, fname, args = {}):
    ext = fname.split('.')[-1].lower()
    return filetypes[ext].save(data, fname, args)

def help(ext):
    filetypes[ext].help()
