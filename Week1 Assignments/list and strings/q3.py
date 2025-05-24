# 3.	Given lst = [('a', 1), ('b', 2), ('a', 3)], convert it into {'a': [1, 3], 'b': [2]} without using defaultdict or setdefault.

lst = [('a', 1), ('b', 2), ('a', 3)]

dict={}
for key,val in lst:
    if key in dict:
        dict[key].append(val)
    else:
        dict[key]=[val]
print(dict)

