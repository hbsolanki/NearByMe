#bank,medical,hospital,station,shop,school,college

class NearByMe:

    def __init__(self):
        self.allPoints=[]
        self.allType=[]
        self.sortType=["Rating","Distance","Rating & Distance"]


    class Point:

        def __init__(self,name,x,y,disciption,type):
            self.x=x
            self.y=y
            #{"Name":"xyz","star":4,"username":"abc"}
            self.reviews=[]
            self.name=name
            self.discription=disciption
            self,type=type

    
    def addPoint(self):
        print()
        print("*-*->New Point Adding : ")
        name=input("Enter Name : ")
        discription=input("Enter Discription : ")
        x=input("Enter x-Cordinate : ")
        y=input("Enter y-Cordinate : ")
        print()
        for i in self.allType:
            print(i)
        print()
        type=input("Choice Above Type Or New Type : ")

        self.allPoints.append(self.Point(name,x,y,discription,type))

    def calculationNearPoint(self,typeNo,sortTypeNo):
        typeName=self.allType[typeNo]
        
        if sortTypeNo=="0":
            pass

        elif sortTypeNo=="1":
            pass
        
        elif sortTypeNo=="2":
            pass

    def userInMap(self,u):
        print()
        print("Near You...")
        
        for i,j in  enumerate(self.allType):
            print((i+1),j)

        print()
        typeNo=int(input("Enter Type Nubmer : "))
        if typeNo<1 and typeNo>len(self.allType):
            print("Invalid Choise Try Again...")
            return
        
        print()
        print("Choice Sorting Type")
        for i,j in  enumerate(self.sortType):
                print((i+1),j)

        sortTypeNo=int(input("Enter Type Nubmer : "))
        if sortTypeNo<1 and sortTypeNo>len(self.sortType):
            print("Invalid Choise Try Again...")
            return


        listOfNearByUs=self.calculationNearPoint(self.allType[typeNo-1],(sortTypeNo-1))
        print()
        print("*-*->This is ")
        for i,j in enumerate(listOfNearByUs):
            print((i+1),"Name :",j.name,"Disciption :",j.disciption,"Review :",j.reviews)

        print()
        print("For Add Review Enter Number or Exit Type 'EXIT'")
        choice=input()

        if choice=="EXIT":
            return
        
        elif int(choice)>0 and int(choice)<len(listOfNearByUs):
            p=listOfNearByUs[int(choice)-1]
        
        else:
            print("Invalid Option Try Again...")



