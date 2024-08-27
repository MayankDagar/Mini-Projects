def fibonacci(n):
  a = 0
  b = 1
  while b<n:
    print(b)
    x = a
    a = b
    b = x+b
fibonacci(15)