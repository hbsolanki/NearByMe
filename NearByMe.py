#bank,medical,hospital,station,shop,school,college
from queue import PriorityQueue

class NearByMe:

    def __init__(self):
        self.allPoints=[]
        self.allType=[]
        # self.sortType=["Rating","Distance","Rating & Distance"]


    class Point:

        def __init__(self,name,x,y,disciption,type,personUsername):
            self.x=x
            self.y=y
            #{"Name":"xyz","star":4,"username":"abc"}
            self.reviews=[]
            self.name=name
            self.discription=disciption
            self.type=type
            self.personUsername=personUsername

    
    def addPoint(self,person):
        print()
        print("*-*->New Point Adding : ")
        name=input("Enter Name : ")
        discription=input("Enter Discription : ")
        x=int(input("Enter x-Cordinate : "))
        y=int(input("Enter y-Cordinate : "))
        print()
        for i in self.allType:
            print(i)
        print()
        sm=input("(1)Choice Above Type (2) New Type : ")
        if sm=="1":
            no=int(input("Enter No Above For Type : "))
            type=self.allType[no]
        elif sm=="2":
            type=input("Enter New Type : ")
            self.allType.append(type)

        self.allPoints.append(self.Point(name,x,y,discription,type,person.username))

    def calculationNearPoint(self,x,y,typeNo):
        typeName=self.allType[typeNo]


        q=PriorityQueue()
        ans=[]


        listOfAvailableType=[]
        for i in self.allPoints:
            if i.type==typeName:
                # listOfAvailableType.append(i)
                dist=((i.x-x)**2)+((i.y-y)**2)
                q.put(dist,i)

        while not q.empty():
# ...         print(q.get()[1].name)
            ans.append(q.get())

        return ans


       

    def userInMap(self,person):
        print()
        x=int(input("Enter x-Cordinate : "))
        y=int(input("Enter y-Cordinate : "))
        print("Near You...")

        print()
        
        for i,j in  enumerate(self.allType):
            print((i+1),j)

        print()
        typeNo=int(input("Enter Type Nubmer : "))
        if typeNo<1 and typeNo>len(self.allType):
            print("Invalid Choise Try Again...")
            return
        
        print()
        # print("Choice Sorting Type")
        # for i,j in  enumerate(self.sortType):
        #         print((i+1),j)

        # sortTypeNo=int(input("Enter Type Nubmer : "))
        # if sortTypeNo<1 and sortTypeNo>len(self.sortType):
        #     print("Invalid Choise Try Again...")
        #     return



        #Calculating Point By Sort Distance
        listOfNearByUs=self.calculationNearPoint(x,y,typeNo-1)
        print(listOfNearByUs)
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
            print()
            print()
            star=int(input("Enter Integer 0-5 Start : "))
            # {"Name":"xyz","star":4,"username":"abc"}
            if star>0 and star<5:
                p.reviews.append({"Name":person.name,"star":star,"username":person.username})
            else:
                print("Invalid Star Choice Try Again...")

            
        
        else:
            print("Invalid Option Try Again...")


    


