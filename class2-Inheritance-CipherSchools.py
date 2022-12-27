class A:
  def __init__(self, x):
    print("A init executed")
class B(A):
  def __init__(self):
    print("B init executed")

abc =B()


class A:
  pass

class B(A):
  pass

class C(B):
  pass

class D(A):
  x = 10

class E(C, D):
  pass

e = E()
print(e.x)




a = range(5)
it = a.__iter__()
it


a = [1, 2, 3, 4]
iter(a)



class myrange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return myrange_iterator(self)

class myrange_iterator:
  def __init__(self, myrange):
    self.myrange = myrange
    self.i = 0

  def __next__(self):
    ret = self.i
    self.i += 1

    if ret >= self.myrange.n:
      raise StopIteration

    return ret


for i in myrange(5):
  print(i)