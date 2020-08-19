# 1.Puedo utilizar el destrcuturing con cualquier colección de datos, pero no es muy recomendable que lo utilice con los
#sets puesto que no poseen un orden definido

currencies = 0.8, 1.2
usd, eur = currencies
print(usd, eur)

friends = [
    ("Rolf", 25),
    ("Anne", 37),
    ("Charlie", 31),
    ("Bob", 22)
]

for name, age in friends:
    print(f"{name} is {age} years old")

# 2.Cuando quiero ignorar un valor de una colección a la hora de usar el destructuring uso _ (así como se hace con el for)

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)

# 3.El * lo ocupo para tomar ciertos valores de un colección a la hora destructurarla, y guardar el resto
# en otra variable

print("Head, *tail -----------------------------------")
head, *tail = [1,2,3,4,5]
print(head)
print(tail)

print("*Head, tail -----------------------------------")
*head, tail = [1,2,3,4,5]
print(head)
print(tail)

print("Head, *middle, tail -----------------------------------")
head, *middle, tail = [1,2,3,4,5]
print(head)
print(middle)
print(tail)

print("first, second, third, *rest -----------------------------------")
first, second, third, *rest = [1,2,3,4,5]
print(first)
print(second)
print(third)
print(rest)