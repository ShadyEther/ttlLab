#check for strong number
def factorial(n):
    fact=1
    while n>1:
        fact*=n
        n-=1
    return fact

# print(factorial(5))

def strong_check(num):
    m=num
    sum_of_digits=0

    while m>0:
        sum_of_digits+=(factorial(m%10))
        m//=10
    return sum_of_digits==num

print(strong_check(40585))