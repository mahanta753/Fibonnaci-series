n =int(input("How many terms you want for Fibonacci Series"))
a,b = 0,1
sum = 0
if(n<=0):
    print("Please.. Enter a positive integer")
    
elif(n==1):
    print("Fibonacci sequence upto",n,":")
    print(a)

else:
    print("The Fibonacci Sequence is :")
    while sum<n:
        print(a)
        c=a+b
        a=b
        b=c
        sum+=1
        
