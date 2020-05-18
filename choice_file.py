
from code_file import*




def menu():

    def options(choice):
    
        if choice == 1:
            a = int(input("Enter The Number"))
            prime(a)
            print("\n")
            menu()
        elif choice ==2:
            a = int(input("Enter The Number"))
            armstrong(a)
            print("\n")
            menu()
        elif choice == 3:
            a = int(input("Enter The Number"))
            reverse(a)
            print("\n")
            menu()
        elif choice == 4:
            a = int(input("Enter The Number"))
            square(a)
            print("\n")
            menu()
        elif choice == 5:
            a = int(input("Enter The Number"))
            sod(a)
            print("\n")
            menu()
        elif choice == 6:
            a = int(input("Enter The Number"))
            cube(a)
            print("\n")
            menu()
        elif choice == 7:
            a = int(input("Enter The Number"))
            palindrome(a)
            print("\n")
            menu()
        elif choice == 8:
            a = int(input("Enter The Number"))
            evenodd(a)
            print("\n")
            menu()
        elif choice == 9:
            a = int(input("Enter The Number"))
            table(a)
            print("\n")
            menu()
        elif choice == 10:
            a = int(input("Enter The Number"))
            factorial(a)
            print("\n")
            menu()
        elif choice == 0:
            a= int(input("Enter The Number"))
            print("exit")
    
        else:
            print("You Enter The Wrong Choice Try Again")


    print("\n")
    print("********************SOME_BASIC_OPERATIONS_ON_NUMBERS************************")
    print("1. To Check Whether Number Is Prime Or Not")
    print("2. To Check Whether Number Is Armstrong Or Not")
    print("3.  Check Whether Number Is Reverse Or Not")
    print("4. Square Of The Number")
    print("5. Sum Of The Digits")
    print("6. Cube Of The Number")
    print("7. Check Whether Number Is Palindrome Or Not")
    print("8. To Check Whether Number Is Even Or Odd ")
    print("9. Table Of The Number")
    print("10.Factorial Of The Number")
    print("0. Exit")
    print("***********************************************************************\n")
    choice = int(input("Enter Your Choice"))
    if choice >0:
        options(choice)
    else:
        return 0



            
