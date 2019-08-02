import csv


def load(fname, args):
    result = []
    with open(fname, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(dict(row))
    return result


def save(data, fname, args):
    with open(fname, 'w', newline='') as f:
        try:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        except:
            raise Exception("Problem writing data to .csv file\n\tMake sure data is formated as a list of dicts")

def help():
    print('CSV reader/writer\n\tload(fname): returns list of dicts\n\tsave(data, fname): data must be a list of dicts')
