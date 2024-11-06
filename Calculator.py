def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Can't divide with denominator Zero(0)"
    else:
        return x/y
while True:
    print("Enter first number(X):")
    x=int(input())
    print("Select the operator :\n+\n-\n*\n/\n")
    o=input()
    print("Enter the second number(Y):")
    y=int(input())
    if o =="+":
        result=add(x,y)
    elif o=="-":
        result=subtract(x,y)
    elif o=="*":
        result=multiply(x,y)
    elif o=="/":
        result=divide(x,y)
    else: 
        print("Enter a valid operator...") 
    print(f"{x} {o} {y} = {result}")
    break 