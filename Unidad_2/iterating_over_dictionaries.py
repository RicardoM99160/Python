friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

# 1.Obtener solo las llaves del diccionario
print("1. Solo las llaves ----------------------------")
for key in friend_ages:
    print(key)

# 2.Obtener solo los valores del diccionario
print("2. Solo los valores ---------------------------")
for value in friend_ages.values():
    print(value)

# 3.Obtener las llaves y los valores del diccionario
print("3. llaves y valores ---------------------------")
for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")