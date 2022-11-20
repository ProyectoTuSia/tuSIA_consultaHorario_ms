from pymongo import MongoClient


def get_db_handle():
#def get_db_handle(db_name, host, port, username, password):

#  client = MongoClient('mongodb+srv://jurinconor:0phnex3dqApDiMuP@cluster0.eb4hb.mongodb.net/?retryWrites=true&w=majority')
 client = MongoClient('mongodb://35.222.42.133:27017')
#define DB name

# mongodb+srv://jurinconor:0phnex3dqApDiMuP@cluster0.eb4hb.mongodb.net/?retryWrites=true&w=majority
 dbname = client['tuSIA_consultaHorario_db']
 #define DB collection
 collection = dbname['schedules']

 return dbname, collection, client