# Calculate the sum of N numbers using while loop and user input.

n=(int(input("enter num:")))
s=0
while (n>=0):
    s+=n
    n=n-1
print("sum=",s)