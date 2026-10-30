class Employee:

  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  @property  # Yeh ban gaya getter method
  def email(self):
    return f"{self.fname}.{self.lname}@company.com"


e = Employee("Arham", "Khan")

# Dekhein! Ab brackets () ki zaroorat nahi parhi, seedha variable ki tarah likha hai:
print(e.email)  # Output: Arham.Khan@company.com