square=[1,4,9,16,25]
print(square)
print(type(square))
print(square[0]) # print element at 0th index
print(square[4]) # print element at 4th index
#print(square[5]) will generate error of index out of range
print(square[-2])# will print second value from right side or back
print(square[1:3]) # slicing 1 is start index whereas 3 is stopped index with exclusion
print(square[1:]) # it will print list starting from 1st index
print(square[:3]) # it will print list starting from 0th index and ends at 2nd index
print(square[-2:])#it will start printing list from second last value
print(square[:-2])#it will start print from 0th index and will stop at second last value
print(square[::2]) #it will start printing list from 0th index with jump of two
print(square[::-2])#it will start printing list from last index with jump of two
print(square+[6**2])#it will concatenate square of 6 in existing list
print(square+["Hello"])#it will concatenate square and hello
#print(square+"Hello") #it will generate error as trying concatenate list with string
square[3:4]=[]
print(square)
#______________________________List Methods______________________________________________#
 #append(x)
 #it add an element at the end of existing list
square.append(34) # will add 34 at the end of existing list
square.append([2,7])#it will add list as an element at the last of list
print(square)

#extend(iterable)
#it flatten the iterables like list,tuples and add each individual elemets at the last of existing list
#square.extend(44) # error as object in extend is not iterable
square.extend([2,7])
print(square)

# insert(index,value): will insert given value at given index
square.insert(2,'a')
print(square)

   # remove(value)
square.remove('a')
print(square)

  # pop(index) remove element from given index
square.pop(5)
print(square)
   # clear()
square.clear()
print(square)

   # index(value)
square=[1,4,9,16,25,4,25]
print(square.index(25))

# count(value)
print(square.count(30))

# sort() //reverse=false or true
square.sort(reverse=True)
print(square)

# reverse()
square.reverse()
print(square)
# copy()
copyList=square.copy()
print(copyList)


color=['red','black','blue']
color2=color #
print(color2)