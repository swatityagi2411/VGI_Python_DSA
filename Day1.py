#Variable declaration with data type
v1=2
print(v1)
v2="VGI"
print(v2)
v3=2.5
print(v3)
v4=True
print(v4)


#How to identify data type of variable
print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))
v5='10'
print(type(v5))

#Operators
#Arithematic Operations
print(10+20) #30,adding 2 values
print(10-20) # -10,subtracting second value from first
print(10*20) #200 multiplying first value with second
print(20/10) #2 first value being divided by second and return quotient
print(20%10) #0 first value being divided by second and return remainder
print(2%3) #2 as if Divisor is greater than divident thn divident will be return as remainder

#Relational operators
print(2>3) #False
print(2<3) #True
#print(2=3) #Error as we are trying to assign one constant to another
#print(a=3)
print(2==3) #False
print(2>=3) #True
print(2<=3) #False

#Bitwise operators
print(200&100)
print(2|3)


#a=(2>3 && 2==2)
#print(a)


#Assingment or initialization of values
a,b=10,20
print(a,b)
#a=b
#b=a

#Swapping of 2 variables
a,b=b,a
print(a,b)

#How python handles multiple assignment to one variable
c=10,20
print(c)

#Type casting Explicit
a="10"
a= int (a)
#a="Hello"//implicit
#print (a)
print(type(a))
x,y=10,20

#Seperator changes
print(x,y,sep='-')


#How to take input in python
z=int(input("Enter value for first integer"))
print(type(z))

#Conditional Statements

num1,num2=20,30
if num1>num2 :
 print("Number 1 is greater")
 print("Thanks")
