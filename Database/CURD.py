import pymongo


#Connection With Database
print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
print(client)
db=client["NearBy"]
collection=db["NearMe"]


def personStoreInDB(p):
    # name,username,password,mobile):
    collection.insert_one({"name":p.name,"username":p.username,"password":p.password,"mobile":p.mobile})

def getPersonDataFromDB():
    data=collection.find({})
    return data

def pointStoreInDB(p):
    # name,x,y,disciption,type,personUsername
    collection.insert_one({"name":p.name,"x":p.x,"y":p.y,"disciption":p.disciption,"type":p.type,"personUsername":p.personUsername})

def getPointFromDB():
    data=collection.find({})