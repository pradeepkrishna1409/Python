

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# Display the first 15 Fibonacci numbers.
#for c in range(0, 15):
    #print(fibonacci(c))


# def fib(n):
#  a,b = 1,1
#  for i in range(n-1):
#   a,b = b,a+b
#  return a
#
# for i in range(10):
#     print fib(i)




## Recursion


def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

for i in range(1,10):
    print(recur_fibo(i))







