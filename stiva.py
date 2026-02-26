class Element:
    def __init__(self,data):
        self.data=data
        self.succ=None

class Stiva:
    def __init__(self):
        self.head=None
        self.size=0

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def push(self, data):
        p=Element(data)
        if self.head:
            p.succ=self.head
        self.head=p
        self.size+=1

    def pop(self):
        if self.isEmpty():
            return "Stiva este goala"
        val=self.head.data
        self.head=self.head.succ
        self.size-=1
        return val

    def top(self):
        if self.isEmpty():
            return "Stiva este goala"
        return self.head.data