#5.	Encode a string such that consecutive runs of 3+ characters are compressed (e.g., "aaabbcccc" → "a3bbc4").

s=(input("enter a string:"))
newS=[]
i=0
while i<=len(s):
    count=1
    