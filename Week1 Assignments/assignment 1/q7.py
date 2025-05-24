# Write a program to check if a number is power of 2.
def ispow2(n):
    if n<=0:
        return False
    i=0
    while 2**i<=n:
        if 2**i==n:
             return True
        i+=1
    return False
n=int(input("enter a num:"))
if ispow2(n):
        print(n,"is power of 2")
    
else:
    print(n,"is not power of 2")