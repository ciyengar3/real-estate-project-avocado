import pymongo as pm

WEBAPP_DBNAME = 'heroku_xp16ghf0'
JOKERZ_DBNAME = 'test'
MONGO_URI = "mongodb://heroku_xp16ghf0:945adf9bpfpp71ror9df1fibhe@ds017886.mlab.com:17886/heroku_xp16ghf0"

active_db_connection = None


def connect_to_database():
    global active_db_connection
    db_instance = None
    try:
        db_instance = pm.MongoClient(MONGO_URI)[WEBAPP_DBNAME]
    except pm.errors.ConnectionFailure:
        print("Connection failure")
        #handle some error
    active_db_connection = db_instance


def get_db_connection():
    global active_db_connection
    return active_db_connection
