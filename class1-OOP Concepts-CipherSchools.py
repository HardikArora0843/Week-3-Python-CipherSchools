a = 5
def func():
  pass
type(func)

class A:
  name = "harsha"
  marks = 50
type(A)


A = 5
type(A)



class A:
  def __call__(self):
    print("You called me")
a = A()
type(a)
a()



a = {"name": "harsha"}
a["name"]



class Exponent:
  def __init__(self, n):
    self.n = n
  
  def __getitem__(self, x):
    return x ** self.n

e = Exponent(3)
e[6]



class Dog:

  tricks = []
  def __init__(self, name):
    self.name = name
  
  def add_trick(self, trick):
    self.tricks.append(trick)

d1 = Dog("Bruno")
d1.add_trick("fetch")
d1.add_trick("walk")
d1.tricks




d2 = Dog("Maxx")
d2.tricks