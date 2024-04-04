import pymongo


#Connection With Database
print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
print(client)
db=client["NearBy"]
collection=db["NearMe"]


def personStoreInDB(p):
    # name,username,password,mobile):
    collection.insert_one({"Person":"p","name":p.name,"username":p.username,"password":p.password,"mobile":p.mobile})

def getPersonDataFromDB():
    data=collection.find({"Person":"p"})
    return data

def pointStoreInDB(p):
    # name,x,y,disciption,type,personUsername
    collection.insert_one({"Point":"p","name":p.name,"x":p.x,"y":p.y,"discription":p.discription,"type":p.type,"personUsername":p.personUsername,"reviews":{}})

def getPointFromDB():
    data=collection.find({"Point":"p"})
    return data

def storeTypeInDB(name):
    collection.insert_one({"Type":"t","name":name})

def getTypeNameFromDB():
    data=collection.find({"Type":"t"})
    return data

def reviewUpdateInDB(p):
    collection.update_one({"Point":"p","name":p.name},{"$set" :{"reviews":p.reviews}})

# collection.delete_many({})