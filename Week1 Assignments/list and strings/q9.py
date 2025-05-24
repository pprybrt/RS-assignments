# 9.	Determine if two strings are anagrams without sorting.(Take two strings of your choice)
def isanagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count={}
    for c in s1:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
    for c in s2:
        if c not in count or count[c]==0:
            return False
        count[c]-=1
    for val in count.values():
        if val!=0:
            return False
    return True
print(isanagram("pat","tap"))

