from pymongo import MongoClient

def userDb():
    mongoClient = MongoClient('127.0.0.1', 27017)
    db = mongoClient['mysitedb']
    user = db['user']
    #user.find_one({'nom':'faneva'})
    return user

user = userDb()
print(user.find_one({'nom':'Nazirah'}))