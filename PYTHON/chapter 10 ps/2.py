class calculators:
    def __init__(self,n):
        self.n=n
    def square(self):
            print(f"the square of a number is:{self.n*self.n}")
    def cube(self):
            print(f"the cube of a number is:{self.n*self.n*self.n}")
    def squareroot(self):
            print(f"the squareroot of a number is:{self.n**1/2}")
    @staticmethod
    def hello():
          print("hello world")        
a=calculators(6)
a.square()   
a.cube()
a.squareroot()   
a.hello()      