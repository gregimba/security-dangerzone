try:
    import cpickle as pickle
else:
    import pickle

db = []

def load():
    db = pickle.load(open("db.pkl","wb"))

def dump():
    pickle.dump(db,open("db.pkl","wb"))
