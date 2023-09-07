n=int(input("Enter first number "))
m=int(input("Enter second number "))

for i in range(m,1,-1):
    if n%i==0 and m%i==0:
        print("GCD is",i)
        break
        
