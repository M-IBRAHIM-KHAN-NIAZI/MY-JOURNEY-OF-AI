class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Yahan humne '+' operator ko overload kiya hai (__add__ ke zariye)
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)

# Jab hum p1 + p2 karenge, toh Python khud-ba-khud __add__ function ko chala dega!
p3 = p1 + p2
print(p3.x, p3.y)  # Output: 4 6