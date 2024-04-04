import NearByMe as NBM
from util import checkMobileNumber,checkPassWord,checkUserName,encodingPassWord
from Database import CURD
class Main:
    def __init__(self):
        # self.allUser=[]
        self.allAdmin=[]
        self.nearByMe=NBM.NearByMe()


    class Person:

        def __init__(self,name,username,password,mobile):
            self.name=name
            self.username=username
            self.password=password
            self.mobile=mobile

    def reStart(self):
        data=CURD.getPersonDataFromDB()
        for i in data:
            self.allAdmin.append(self.Person(i["name"],i["username"],i["password"],i["mobile"]))

        # ,name,x,y,disciption,type,personUsername
        allPoint=CURD.getPointFromDB()
        for i in allPoint:
            print(i)
            p=self.nearByMe.Point(i["name"],i["x"],i["y"],i["discription"],i["type"],i["personUsername"])
            if i["reviews"] :
                p.reviews=i["reviews"]
            self.nearByMe.allPoints.append(p)

        allType=CURD.getTypeNameFromDB()
        for i in allType:
            self.nearByMe.allType.append(i["name"])


    def main(self):
        choice=None
        self.reStart()
        self.admin()


    def admin(self):

        choice=input("(1)Already Admin (2)New Admin : ")
        if choice=="1":
            print("Username must be small  ")
            username=input("Enter UserName : ")
            while(not checkUserName(username)):
                print("Username must be small  ")
                print("Invalid Username Type ...")
                username=input("Enter UserName : ")

            print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character  ")
            password=input("Enter PassWord : ")
            while(not checkPassWord(password)):
                print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character ")
                print("Invalid Password Type ...")
                password=input("Enter PassWord : ")


            password=encodingPassWord(password)
            for i in self.allAdmin:
                if i.username==username and i.password==password:
                    self.adminInMap(i)
                    return
            else:
                print("This UserName And PassWord Not Valid Try agin...")

        elif choice=="2":
            print()
            print("*-*->New Registration")
            name=input("Enter Name : ")
            print("Username must be small  ")
            username=input("Enter UserName : ")
            while(not checkUserName(username)):
                print("Username must be small ")
                print("Invalid Username Type ...")
                username=input("Enter UserName : ")

            print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character ")
            password=input("Enter PassWord : ")
            while(not checkPassWord(password)):
                print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character ")
                print("Invalid Password Type ...")
                password=input("Enter PassWord : ")

            mobile=input("Enter Mobile Number : ")
            while(not checkMobileNumber(mobile)):
                print("Mobile Number Must Be 10 Digit And All Integer...")
                print("Invalid Mobile Number Type ...")
                mobile=input("Enter Mobile Number : ")

            a=self.Person(name,username,encodingPassWord(password),mobile)
            self.allAdmin.append(a)
            CURD.personStoreInDB(a)
            print("Registation Sucessfuly Completed")
            self.adminInMap(a)
            
        
    def adminInMap(self,a):
        smChoice=""
        while smChoice!=3:
            print()
            smChoice=input("(1)Add Point (2)Find Near You (3)Exit \n")

            if smChoice=="1":
                self.nearByMe.addPoint(a)

            elif smChoice=="2":
                self.nearByMe.userInMap(a)

            elif smChoice=="3":
                break

            else:
                print("Invalid Option...")

Main().main()