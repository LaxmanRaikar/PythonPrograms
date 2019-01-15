class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None

class rcb:
    def __init__(self):
        self.headval= None


    def kk(self):
        printval=self.headval
        while printval and not None:
            print(printval.dataval)
            printval=printval.nextval
    def AtBegning(self,newdata):
        NewNode=node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode



list1 = rcb()
list1.headval=node("mon")
e2=node("tue")
e3=node("wed")
list1.headval.nextval=e2
e2.nextval=e3
list1.AtBegning("sun")
list1.kk()


