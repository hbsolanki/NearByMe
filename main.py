import NearByMe as NBM

class Main:
    def __init__(self):
        self.allUser=[]
        self.allAdmin=[]

    def main(self):
        choice=None
        while choice!=3:
            print()
            choice=input("(1)User \n(2)Admin \n(3)Exit")

            if choice=="1":
                self.user()

            elif choice=="2":
                self.admin()

            elif choice=="3":
                break

            else:
                print("Choice Valid Option")


    def user(self):
        pass

    def admin(self):

        choice=input("(1)Already Admin \n(2)New Admin : ")
        if choice=="1":
            username=input("Enter UserName : ")
            password=input("Enter PassWord : ")
            for i in self.allAdmin:
                if i.username==username and i.password==password:
                    pass
                    break
            else:
                print("This UserName And PassWord Not Valid Try agin...")

        elif choice=="2":
            print()
            print("*-*->New Registration")
            name=input("Enter Name : ")
            username=input("Enter UserName : ")
            password=input("Enter PassWord : ")
            mobile=input("Enter Mobile Number : ")

            print("Registation Sucessfuly Compated")
            
        
                