def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y=1):
    return x*y

def divide(*x,**y):

    if y['y']!=0:
        return x[0]/y['y']
    else:
        return "Err: Divide by zero"


n1=3
n2=4

print(add(1,2))
print(sub(n1,n2))
print(multiply(x=n1,y=n2))
print(multiply(x=n1))
print(divide(6,y=3))

