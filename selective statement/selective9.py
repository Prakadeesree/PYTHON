bill=int(input("enter the bill amount"))
food=int(input("enter the food rating"))
service=int(input("enter the service rating"))
ambience =int(input("enter the ambience rating"))
if((food==4)or(food==5)):
    if((service==(4 or 5))and(ambience==(4 or 5))):
        print("the tip is",bill*(10/100))
    else:
        print("the tip is",bill*(5/100))
if((food==1)or(food==2)or(food==3)):
    if((service==(4 or 5))and(ambience==(4 or 5))):
        print("the tip is",bill*(5/100))
    else:
        print("the tip is",bill*(1/100))
    



