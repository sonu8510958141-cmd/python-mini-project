temp=0
def armstrong(num):
    temp=num
    total=0
    while temp>0:
     digit=temp%10
     total=total+digit**3
     temp=temp//10
    return total==num
def operation(a,b,choice):
    if choice==1:
        return a+b
    elif choice==2:
        return a-b
    elif choice==3:
        return a*b
    elif choice==4:
        return a/b
    elif choice==5:
        exit()
    else:
        print ("your data is not  mismatch")
try:
    num=input("enter your any number :")
    if num ==3 and not num.isdigit():
      print("error your any number")
    else:
        num=int(num)
    if armstrong(num):
         print(f"your {num } is armstrong")
    else:
        print(f"your {num} not armstong")
    # print("1. add") 
    # print("2. subtract")
    # print("3. multiplication")
    # print("4. divided")     
    # print("5. exit")
    # choice=int(input("enter your choice no"))
    # a=int(input("enter your any numbers"))
    # b=int(input("enter your any numbers"))
    # result=operation(a,b,choice)
    # print("result=",result)
except ValueError:
   print("your data is not match in this no")     
except Exception as e:
          print(f"an unexpected error occureed{e}")   