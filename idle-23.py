'''set is a type of collection of elements without duplicate values
also without an order, index and all the elements are inluded as
unique elements
set itself is mutable(addable / reamovable elements)'''

set1 ={1,2,3,4,5}
set2 ={4,5,6,7,8}

print("Union:", set1 | set2)

print("inetrsection:", set1 & set2)

print("difference (set1-set2):", set1-set2)

print("symmetric difference:", set1^set2)
