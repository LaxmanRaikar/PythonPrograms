class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class linkedlist:
    def __init__(self):
        self.headval=None

    def printList(self):
        temp = self.headval
        while (temp):
            print(temp.dataval)
            temp = temp.nextval

if __name__ == '__main__':

    list=linkedlist()
    list.headval=node(1)
    second=node(2)
    third=node(3)
    list.headval.nextval=second
    second.nextval=third
    list.printList()

