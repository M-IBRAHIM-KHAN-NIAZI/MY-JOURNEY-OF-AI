class hero():
    hero="microsoft"
    def arham (self):
        print(f"the name of a company is:{self.arham}")
class zero():
    salary=120000
    def c (self):
        print(f"the salary of a company is:{self.c}")

class villian(hero,zero):

    company="google"
    def b (self):
        print(f"the name of a company is:{self.b}")

b=villian()
print(b.company,b.hero,b.salary)





