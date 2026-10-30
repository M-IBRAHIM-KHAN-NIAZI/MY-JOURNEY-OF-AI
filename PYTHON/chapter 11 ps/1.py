class twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector of i is {self.i}i.the vector of  j is {self.j}j.  ")    
class threedvector(twodvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k     
    def show(self):
            
            print(f"the vector of i is {self.i}i.the vector of  j is {self.j}j.the vector of k is {self.k}k  ")   
a=twodvector(2,7)
b=threedvector(2,9,11)
a.show()
b.show()                