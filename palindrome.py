def is_palindrome(num):
    original= num
    reverse = 0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10 
    return original==reverse  
def opreation(a,b,choice):
            if choice==1:
                return a+b
            elif choice==2:
                 return a-b
            elif choice==3:
                 return a*b
            elif choice==4:
               if b==0:
                return a/b
            elif choice==5:
                return"exit now"
            else:
                 return"error divided in not by zero or your data is invalid"
try:
    num=input("enter your any six digit number:")
    if len(num)!=6 or not num.isdigit():
        print("error:only 6 number is allowed")
        exit()
    else:
        num=int(num)
        # palindrome check now
        if is_palindrome (num):
            print(f"your num {num}is palindrome")
        else:
            print(f" your no {num}is not a palindrome")
    print("\n======= operation menu ======") 
    print("1. add") 
    print("2. subtract")
    print("3. multiplication")
    print("4. divided")     
    print("5. exti")
    choice=int(input("enter your choice no"))
    a=int(input("enter your any numbers"))
    b=int(input("enter your any numbers"))
    result=opreation(a,b,choice)
    print("result=",result)
except ValueError:
    print("error: please enter valid numbers")
except Exception as e:
     print(f"an unexpected error occureed{e}")


         