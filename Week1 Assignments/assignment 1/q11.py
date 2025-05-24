# write a program to swap elements inside each tuple

tpl=[(1,2),(3,4),(5,6)]
swap=[(y,x) for (x,y) in tpl]
print("after swapping:",swap)