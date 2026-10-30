class Employee:

  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def email(self):
    print (f"{self.fname}.{self.lname}@company.com")


e = Employee("Arham", "Khan")

# Yahan brackets () lagana LAZMI hai kyunki yeh ek function hai:
print(e.email())  # Output: Arham.Khan@company.com