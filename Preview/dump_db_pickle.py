import pickle

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
