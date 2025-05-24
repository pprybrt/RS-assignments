#  Write a Python function that checks whether all elements in a given list are unique using a set

def unique(lst):
    return len(lst)==len(set(lst))
lst=[1,2,3,4,3]
if unique(lst):
    print("all elements are unique in the list")
else:
    print("duplicate elemnts are present in the list")
