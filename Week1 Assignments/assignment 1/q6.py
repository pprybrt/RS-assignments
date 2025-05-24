#  Given a list, and dictionary and a Key K, print the value of K from the dictionary if the key is present in both, the list and the dictionary.

lst=["a","b","c"]
dct={"a":1,"b":2,"d":3}
K=input("enter key:")
if K in lst and K in dct:
    print(f"value of {K}= {dct[K]}")
else:
    print(f"{K} is not present in both list and dictionary!")