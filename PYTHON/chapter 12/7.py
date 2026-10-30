# 1. Apna khud ka custom error class banana
class InvalidAgeError(Exception):
    pass
    

# 2. Isko apne code mein istemal karna
try:
    age = 15
    if age < 18:
        raise InvalidAgeError("Age 18 se kam nahi honi chahiye!")
except InvalidAgeError as e:
    print(f"Custom Error Caught: {e}")