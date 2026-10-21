p1="have a lot of money"
p2="buy now"
p3="chutiya"
message=input("enter your comment: ")
if p1 in message or p2 in message or p3 in message:
    print("This comment is not allowed")
else:
    print("This comment is allowed")