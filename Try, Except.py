'''try:
    age = int(input("age: "))
    income = 2000
    risk = income / age         
    print(age)
except ValueError:
    print("Invalid Value",)
except ZeroDivisionError:
    print ("Age cannot be 0.")

print("#" * 25)'''

########################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw (self):
        print("draw")
    def move (self):
        print("move")


point = Point()
point.move()
point.draw()
point1 = Point()
print(point1)

