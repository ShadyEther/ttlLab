#armstrong range
range1=int(input("range1= "))
range2=int(input("range2= "))

for _  in range(range1,range2):
    m=_
    digits=0
    while m>0:
        digits+=1
        m//=10

    m=_
    sum_of_digits=0
    while m>0:
        sum_of_digits=sum_of_digits+((m%10)**digits)
        m//=10
        
    if sum_of_digits==_:
        print(_)