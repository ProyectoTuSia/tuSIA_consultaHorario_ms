from pymongo import MongoClient


def get_db_handle(method):
#def get_db_handle(db_name, host, port, username, password):

#  client = MongoClient('mongodb+srv://jurinconor:0phnex3dqApDiMuP@cluster0.eb4hb.mongodb.net/?retryWrites=true&w=majority')
#  client = MongoClient('mongodb://35.203.71.115:27017/?replicaSet=rs0&readPreference=secondary')

    if method=='PUT':
        client = MongoClient(
        'mongodb://10.162.0.5:27017')
        print("the method is"+method)
        print("IP 10.162.0.5:27017")
        # replicaSet='rs0',
        # readPreference='secondary')
    else:
        client = MongoClient(
        'mongodb://10.162.0.6:27017')
        print("the method is"+method)
        print("IP 10.162.0.6")

        # replicaSet='rs0',
        # readPreference='secondary')

    dbname = client['tuSIA_consultaHorario_db']
    #define DB collection
    collection = dbname['schedules']

    return dbname, collection, client