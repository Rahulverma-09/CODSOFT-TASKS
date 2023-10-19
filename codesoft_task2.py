                                       #----SIMPLE CALCULATOR-----

# TAKE TWO NUMBER FROM USER--

num1=int(input("ENTER FIRST NUMBER : "))
num2=int(input("ENTER SECOND NUMBER : "))

# THIS IS A FUNCTION THAT PERFORM ALL MATHEMATICS OPERATION ACCORDING TO THE CHOICE OF A USER--

def opt():
    choice=str(input("CHOOSE OPERATION - \n1-'+'\n2-'-'\n3-'*'\n4-'/'\nENTER OPERATION : "))
    if choice=='+':
        print(num1,choice,num2,"=",num1+num2)
    if choice=='-':
        print(num1,choice,num2,"=",num1-num2)
    if choice=='*':
        print(num1,choice,num2,"=",num1*num2) 
    if choice=='/':
        if num1%num2==0:
            print(num1,choice,num2,"=",int(num1/num2))
        else:
            print(num1,choice,num2,"=",num1/num2) 
            exit;
    if choice!='+' and choice!='-' and choice!='*' and choice!='/':
        print("PLEASE CHOOSE RIGHT OPEARTION FROM THE GIVEN!!!\n")
        opt()
opt()               