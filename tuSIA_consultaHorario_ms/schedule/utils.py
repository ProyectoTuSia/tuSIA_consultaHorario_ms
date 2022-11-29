from pymongo import MongoClient


def get_db_handle(method):
#def get_db_handle(db_name, host, port, username, password):

#  client = MongoClient('mongodb+srv://jurinconor:0phnex3dqApDiMuP@cluster0.eb4hb.mongodb.net/?retryWrites=true&w=majority')
#  client = MongoClient('mongodb://35.203.71.115:27017/?replicaSet=rs0&readPreference=secondary')

    if method=='PUT':
        client = MongoClient(
        'mongodb://34.152.30.169:27017')
        print("the method is"+method)
        print("IP 34.152.30.169")
        # replicaSet='rs0',
        # readPreference='secondary')
    else:
        client = MongoClient(
        'mongodb://35.203.48.229:27017')
        print("the method is"+method)
        print("IP 35.203.48.229")

        # replicaSet='rs0',
        # readPreference='secondary')

    dbname = client['tuSIA_consultaHorario_db']
    #define DB collection
    collection = dbname['schedules']

    return dbname, collection, client