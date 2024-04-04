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


    def main(self):
        choice=None
        self.reStart()
        self.admin()
        # while choice!=3:
        #     print()
        #     choice=input("(1)User (2)Admin (3)Exit \n")

        #     if choice=="1":
        #         self.user()

        #     elif choice=="2":
        #         self.admin()

        #     elif choice=="3":
        #         break

        #     else:
        #         print("Choice Valid Option")


    def user(self):
        choice=input("(1)Already User (2)New User : ")
        if choice=="1":
            print("Username must be small : ")
            username=input("Enter UserName : ")
            while(not checkUserName(username)):
                print("Username must be small : ")
                print("Invalid Username Type ...")
                username=input("Enter UserName : ")

            print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
            password=input("Enter PassWord : ")
            while(not checkPassWord(password)):
                print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
                print("Invalid Password Type ...")
                password=input("Enter PassWord : ")



            for i in self.allAdmin:
                if i.username==username and i.password==password:
                    print()
                    self.nearByMe.userInMap(i)
                    return
            else:
                print("This UserName And PassWord Not Valid Try agin...")

        elif choice=="2":
            print()
            print("*-*->New Registration")
            name=input("Enter Name : ")
            print("Username must be small : ")
            username=input("Enter UserName : ")
            while(not checkUserName(username)):
                print("Username must be small : ")
                print("Invalid Username Type ...")
                username=input("Enter UserName : ")

            print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
            password=input("Enter PassWord : ")
            while(not checkPassWord(password)):
                print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
                print("Invalid Password Type ...")
                password=input("Enter PassWord : ")

            mobile=input("Enter Mobile Number : ")
            while(not checkMobileNumber(mobile)):
                print("Mobile Number Must Be 10 Digit And All Integer...")
                print("Invalid Mobile Number Type ...")
                mobile=input("Enter Mobile Number : ")

            # name,username,password,mobile)
            u=self.Person(name,username,encodingPassWord(password),mobile)
            self.allUser.append(u)

            print("Registation Sucessfuly Compated")
            print()
            self.nearByMe.userInMap(u)
            
        
                

    def admin(self):

        choice=input("(1)Already Admin (2)New Admin : ")
        if choice=="1":
            print("Username must be small : ")
            username=input("Enter UserName : ")
            while(not checkUserName(username)):
                print("Username must be small : ")
                print("Invalid Username Type ...")
                username=input("Enter UserName : ")

            print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
            password=input("Enter PassWord : ")
            while(not checkPassWord(password)):
                print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
                print("Invalid Password Type ...")
                password=input("Enter PassWord : ")



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
            print("Username must be small : ")
            username=input("Enter UserName : ")
            while(not checkUserName(username)):
                print("Username must be small : ")
                print("Invalid Username Type ...")
                username=input("Enter UserName : ")

            print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
            password=input("Enter PassWord : ")
            while(not checkPassWord(password)):
                print("Password must be 8 letter and contain (1 small,1 capital,1 Special) Character : ")
                print("Invalid Password Type ...")
                password=input("Enter PassWord : ")

            mobile=input("Enter Mobile Number : ")
            # while(not checkMobileNumber(mobile)):
            #     print("Mobile Number Must Be 10 Digit And All Integer...")
            #     print("Invalid Mobile Number Type ...")
            #     mobile=input("Enter Mobile Number : ")

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