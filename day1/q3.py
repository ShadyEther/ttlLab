#electricity bill..1st 100 units @2.5perunit..next 100 units @4per unit..next 100@5 per unit
units=float(input("units="))
cost=0
if units<=100:
    cost=units*2.5
elif units<=200:
    cost=100*2.5+(units-100)*4
else:
    cost=100*2.5+100*4+(units-200)*5

print("Cost: ",cost)