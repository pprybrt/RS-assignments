# Given two arrays which are duplicates of each other except one element, that is, one element from one of the array is missing, we need to find that missing element using set. 

l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5]
missing=list(set(l1)^set(l2))
print("missing elem is:",missing)