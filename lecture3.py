### list in python

names = [ "John", "Jane", "Doe" ]
print(names)
print(names[0])
print(len(names))
print(names[-1])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
list.append(11)
list.append([1,2,3])
list.extend([1,2,3])
print(list)


list1 = [1, 2, 3, 4, 5]
list1.insert(1,10)
print(list1)

list2 = [1, 2, 3, 4, 5]
list2.remove(3)
print(list2)
list2.pop(2)
print(list2)

list3 = [1, 2, 3, 4, 5]
print(max(list3))
print(min(list3))

list4 = [ 1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(list4.count(1))
print(list4.count(2))
print(list4.count(3))

list5 = [1, 2, 3, 4, 5,1,2,3,4,5]
list5.sort()
print(list5)
list5.reverse()
print(list5)

list6 = [1, 2, 3, 4, 5]
print(list6[1:4])
print(list6[:3])
print(list6[3:])
print(list6[2:3:5])
print(list6[::-1])


### tuple in python

tuple = [1, 2, 3, 4, 5, "Demon", "Slayer"] 
print(tuple)
print(tuple[0])
print(len(tuple))
print(tuple[-1])
print(tuple[1:4])
print(tuple[:3])

tuple = list(tuple)
tuple.append("Anime")


#### Strings











