#functions and reccursions
def avg():
    n=int(input("Enter the number of elements: "))
    sum=0
    for i in range(n):
        num=int(input("Enter number: "))
        sum+=num
    return sum/n

print("Average:", avg())