# Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 

# HINT: Each inner tuple contains numerical values, and you are to find the average column-wise.

# Original Tuple: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) 

# Average value of the numbers of the said tuple of tuples: [30.5, 34.25, 27.0, 23.25]


tpl=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) 
a,b,c,d=list(tpl)
avga=(sum(list(a)))/len(a)
avgb=(sum(list(b)))/len(b)
avgc=(sum(list(c)))/len(c)
avgd=(sum(list(d)))/len(d)

print(avga,avgb,avgc,avgd)