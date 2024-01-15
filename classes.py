class Point:
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')


point1 = Point()

point1.x = 10
point1.y = 20
point1.draw()
print(point1.x)


#adding a constructor (like js)

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')
    
    def draw(self):
        print('draw')


point2 = Point2(10,20)
print(point2.x)

#challenge

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'hi, I am {self.name}')


john = Person('john smith')
john.talk()

bob = Person('Bob Smith')
bob.talk()
