# Write a Python program that takes a natural number n as input and prints a pattern where each line shows the sum of squares of the first i natural numbers, from 1 to n. (where n ≥ 1). 

n=int(input("enter a number:"))
s=0
for i in range(1,n+1):
    s+=(i**2)
    print(s)