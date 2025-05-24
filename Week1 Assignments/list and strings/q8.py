#8.	Convert a list of words into an acronym (first letters capitalized).
#Example: ["Federal", "Bureau", "Investigation"] → "FBI"

def acronym(words):
    result=''
    l=len(words)
    for j in range(0,l):
        k=words[j]
        result+=k[0].upper()
    return result
print(acronym(["Federal", "Bureau", "Investigation"]))

