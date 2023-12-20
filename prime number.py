def prime(num):
    if num == 1:
        print("it is not a prime number")
    is_prime =True    
    for i in range(2, num):
        if num % i==0:
            is_prime = False
    if is_prime:
        print("prime number")
    else:
        print("not prime number")       
a=int(input())
prime(num=a)    