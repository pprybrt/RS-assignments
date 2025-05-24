# 1.You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False. Note: str contains only lowercase English alphabets.

x=str(input("enter your string:"))
str=x.lower()
if str.count("cat")==str.count("hat"):
    print("True")
else:
    print("False")

