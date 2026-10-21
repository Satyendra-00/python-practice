#updating value of list which is inside set 
s={8,7,12,[1,2,3]} #this will give error because list is mutable and set can only have immutable values
s[3][0]=100
print(s)