class Employee:

  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  @property
  def fullname(self):
    return f"{self.fname} {self.lname}"

  # Yeh hai setter (Value update karne ke liye)
  @fullname.setter
  def fullname(self, value):
    names = value.split(" ")  # ["Ali", "Khan"]
    self.fname = names[1]
    self.lname = names[0]


e = Employee("Arham", "Khan")
print(e.fullname)  # Output: Arham Khan

# Ab hum setter ke zariye direct naya naam set kar rahe hain:
e.fullname = "Ali Khan"
print(e.fname)  # Output: Ali
print(e.lname)  # Output: Khan
print(e.fullname)  # Output: Ali Khan