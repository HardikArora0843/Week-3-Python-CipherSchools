def generate_squares(n):
  return [ i**2 for i in range(1, n) ]

for x in generate_squares(100):
  print(x)
       


def generate_squares(n):
  for i in range(1, n):
    yield i**2
 
for i in generate_squares(10):
  print(i)



a = generate_squares(10)
type(a)



def func():
  print("start")
  yield 1
  print("yielded 1")
  yield 2
  print("yielded 2")

it = iter(func())
next(it)



a = ( i**2 for i in range(10) )
for i in a:
  print(i)


a = ( i**2 for i in range(10) )
iter(a)