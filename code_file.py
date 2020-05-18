


#             TO CHECK PRIME NUMBER

def prime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print("Number is Not Prime")
                break
            else:
                print("Number is prime")

#             TO CHECK ARMSTRONG NUMBER
def armstrong(n):
    temp=n
    sum=0
    for i in range(0,temp):
        digits=temp%10
        sum=sum+digits**3
        temp=temp//10

    if n==sum:
        print("Enter Number is Armstrong")
    else:
        print("Enter Number is Not Armstrong")


#            TO CHECK REVERSE NUMBER
def reverse(n):
   #temp=n
   rev=0
   while n>0:
        digits=n%10
        rev=rev*10+digits
        n=n//10
   print("Reverse Number is ",rev)




#            SQUARE OF THE NUMBER
def square(n):
    c=n*n
    print("The Square of the number ",n,"is =",c)



#           SUM OF DIGITS

def sod(n):
    sum=0
    while n>0:
        digits=n%10
        sum = sum + digits
        n=n//10
    print("Sum Of Digits is ",sum)

#               CUBE OF THE NUMBER
def cube(n):
    c=n*n*n
    print("The cube of the number ",n,"is =",c)



#            TO CHECK  NUMBER IS PALINDROME

def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digits=n%10
        rev = rev*10 + digits
        n=n//10
    if rev==temp:
        print ("Number is Palindrome")
    else:
        print ("Number is NOT Palindrome")


#            TO CHECK ODD EVEN NUMBER

def evenodd(n):
    if n%2==0:
        print("Enter Number Is EVEN")
    else:
        print("Enter Number Is ODD")

#            TABLE

def table(n):
    print("TABLE OF ",n)
    for i in range (0,11):
        print(n,"X",i,"=",n*i)


#           FACTORIAL

def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print("Factorial of the number is",fact)

