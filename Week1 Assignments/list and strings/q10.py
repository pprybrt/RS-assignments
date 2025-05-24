#10.	Given a list of n-1 integers from 1 to n, write the code to find the missing number.
#Example: [1, 2, 4, 5] → 3

l1=[1, 2, 4, 5]
n=(len(l1))+1
x=n*(n+1)//2-sum(l1)
print(x)

