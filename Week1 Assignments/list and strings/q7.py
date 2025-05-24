#7.	Given a list like ["abc", "def", ["ghi", "jkl"]], flatten it into a single list of characters.


lst=["abc", "def", ["ghi", "jkl"]]
result=[]
for item in lst:
    if type(item)==list:
        for subitem in item:
            for ch in subitem:
                result.append(ch)
    else:
        for ch in item:
            result.append(ch)
print(result)