# Write a Python program to count the frequency of each character in a string using a dictionary.

freq={}
n=input("enter a string:")
for char in n:
    freq[char]=freq.get(char,0)+1
print(freq)