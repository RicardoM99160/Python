friends = [
    ["Rolf", 21], 
    ["Bob", 30], 
    ["Anne", 27],
    ["Charlie", 37],
    ["Jen", 25],
    ["Adam", 29]
]

friends.append(["Ricardo", 21])
friends.remove(["Anne", 27])
print(friends)
print(friends[len(friends)-1][0])

l_1 = [1,2,3,4]
l_2 = [5,6,7,8]
t_1 = (9,10,11,12)

print(l_1 + l_2)
#print(l_1 + t_1) Esto da error
l_1.extend(t_1)
print(l_1)