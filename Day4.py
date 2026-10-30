# Tuples
fruits=("Apple","Mango","Grapes")

print(fruits)
print(type(fruits))
#fruits[1]="Berries" # error as tuples are immutable
#fruits.append("Berries") #error as append tries to change tuple which is immutable
print(fruits[1:])
print(fruits[0]) # print element at 0th index
print(fruits[2]) # print element at 4th index
#print(square[5]) will generate error of index out of range
print(fruits[-2])# will print second value from right side or back
print(fruits[1:3]) # slicing 1 is start index whereas 3 is stopped index with exclusion
print(fruits[1:]) # it will print list starting from 1st index
print(fruits[:3]) # it will print list starting from 0th index and ends at 2nd index
print(fruits[-2:])#it will start printing list from second last value
print(fruits[:-2])#it will start print from 0th index and will stop at second last value
print(fruits[::2]) #it will start printing list from 0th index with jump of two
print(fruits[::-2])#it will start printing list from last index with jump of two

cordinates=(23.7856,-3456213)
lat,long=cordinates
print(lat,long)

for i in fruits:
    print(i)


## Dictionary
students={

    "name":"Dennis",
    "age":27,
    "city":"Delhi",
    "skills":["Python","c"]
}

print(students)
print(type(students))

for key in students:
    print(key,students[key])
print(students.get("skills"))

students["marks"]=57 #add new key value pair
students["name"]="Ritchie"# update existing key with new value
print(students)

students.update({"name": "Rohan","age":29})
print(students)

stack=[]
stack.append(10)
stack.append(20)
print(stack)

remove=stack.pop()
print("Element removed is",remove)
print(stack)


def push(stack,item):
    stack.append(item)

def pop(stack):
    remove=stack.pop
    print("removed element is",remove)

push(stack,100)
push(stack,200)
print(stack)
pop(stack)
print(stack)
