class complex():
    def __init__(self,r,i):
        self.i=i
        self.r=r
    def __add__(self, c2):
        return complex ( self.r + c2.r,self.i +c2.i)
    def __str__(self):
        return f"{self.r}+{self.i}i"
    
        
c1=complex(2,3)
c2=complex(5,7)
print(c1+c2)