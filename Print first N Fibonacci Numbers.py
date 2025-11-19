def fibonacci(n):
    if n <= 0:
        return
    a,b = 0,1
    for i in range (n):
        print(a,end =" ")
        a,b = b, a + b
fibonacci(10)               
