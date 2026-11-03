#_______________________Linear Search__________________
# at List

def linearSearch(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return -1

list1=[11,3,14,24,5]
element=int(input("Provide element"))
result=linearSearch(list1,element)

if result==-1:
    print("Element not found")
else:
    print("Found at index",result)

# at Stack:
stack=[]
stack.append[10]
stack.append[20]
for i in range(top,-1):
    if stack[i]==element:
        break
if i>-1:
    print("Found")
else:
    print("not found")

#_____________Binary Search_______________


    

list1=[10,20,30,40,50]
element=int(input("Provide Element"))
result=BinarySearch(list1,element)

if result==-1:
    print("Element not found")
else:
    print("Found at index",result)

#_____________Recursion_________
#when a function call itself than this process is known as recurssion:It comprises of two cases:
#base case:where recursive call ends, General case :where recursive call exists

def factorial(number):
    if number==0||number==1:
        return 1
    else:
        return number*factorial(number-1)

result=factorial(5)
print(result)

#_________________Binary Search using Recursion _______________

def BinarySearch(list,target,low,high):
        if low>high:
            return -1
        
        mid=int((low+last)/2)
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            BinarySearch(list,target,mid+1,high)
        else:
            BinarySearch(list,target,low,mid-1)
    return -1

list1=[10,20,30,40,50]
element=int(input("Provide Element"))
result=BinarySearch(list1,element,0,len(list1))

if result==-1:
    print("Element not found")
else:
    print("Found at index",result)

#___________________________Bubble Sort_______________

def Bsort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)

list1=[11,2,33,21,6,18]
Bsort(list1)

#______________________Selection Sort____________
def Selsort(list):
    for i in range(len(list)-1):
        smallest=a[i]
        for j in range(i,len(list)-1-i):
            if smallest>list[j]:
                smallest=list[j]
                pos=jump
        list[i],list[pos]=list[pos],list[i]
    print(list)

list1=[10,2,54,7,11]
Selsort(list1)