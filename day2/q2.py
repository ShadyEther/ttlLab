add=lambda x,y: x+y
sub=lambda x,y: x-y
mul=lambda x,y: x*y
div=lambda x,y: x/y if y!=0 else "Err: Divide by zero"

list1=list(range(1,10))
print (list(filter(lambda x:x%2==0,list1)))

print(list(map(lambda x:x**2,list1)))

print(sorted(list1,key=lambda x:-x))

