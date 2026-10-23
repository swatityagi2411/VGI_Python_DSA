#Control Statements

#Conditional Statements
#1.if 
age=10
if age>=18:
    print("eligible to vote")
if age<18:
    print("Not eligible")

#2. if-else
age=16
if age>=18:
    print("eligible to vote")
else:
    print("Not eligible")
    # nested if else
    #Find largest number among 3 provided number
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))
    num3=int(input("Enter third number"))
    if(num1>num2):
        if(num1>num3):
            print("Num1 is greatest")
        else:
            print("Num 3 is greatest")
    else:
        if(num2>num3):
            print("num 2 is greatest")
        else:
            print("Num3 is greatest")

# if(num1>num2 and num1>num3)
#    else:
        #if(num2>num1 and num2>num3)
       #else
        #print 
#3 elif

marks=int(input("Provide marks"))
if(marks>=90):
    print("A+")
elif(marks>=70 and marks<=89):
    print("A")
elif(marks>=65 and marks<=69):
    print("B+")
elif(marks>=55 and marks<=64):
    print("B")
else:
    print("Better luck next time")

#Switch
choice=int(input("press 1 for add, press 2 for subtract"))
match choice:
    case 1:print("Addition")

    case 2:print("subtraction")

    case _:print("wrong choice")


    #Loops
    #1.while
num=1
while num<=10:
    print(num)
    num=num+1
    
#for
for i in range(1,11):
    print(i)