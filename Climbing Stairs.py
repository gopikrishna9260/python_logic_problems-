def clim_stairs(n):
    if n <= 2:
        return n
    a,b = 1,2
    for i in range (3,n+1):
        c = a + b
        a = b
        b = c
    return b
print(clim_stairs(10))    
