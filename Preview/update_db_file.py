from make_db_file import loadDbase,storeDbase

db=loadDbase()
db['sue']['pay']*=1.100
db['tom']['name']='Tom Tom'
storeDbase(db)
