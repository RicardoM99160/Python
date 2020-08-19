#Los Sets son colecciones de datos, como las tuplas y los arreglos, con la diferencia que no poseen un orden y no contienen elementos repetidos
#Un Set se declara usando {} (llaves)
# 1.Como los Sets no poseen orden, pueda ser que cada vez que se muestren por pantalla, los elementos que los contengan se muestren en diferente orden
art_friends = {"Rolf" , "Anne"}
science_friends = {"Jen", "Charlie"}
print("1: ", art_friends,science_friends)

# 2.Agregar un elemento al Set
art_friends.add("Ricardo")
print("2: ", art_friends)

# 3.Agregar más de un elemento al Set
art_friends.update(["Carlos", "Andrea"])
print("3: ", art_friends)

# 4.1.Eliminar un elemento del Set
art_friends.remove("Rolf")
print("4: ", art_friends)

# 4.2.Discard es igual que remove, con la diferencia que discard elimina el elemento si este existe, en caso contrario no hace nada.
art_friends.discard("Carlos")
print("4.2: ", art_friends)

# 4.3.Pop elimina un elemento aleatorio del Set
random_art_friend = art_friends.pop()
print("4.3: ", random_art_friend, art_friends)

# 4.4.Clear elimina todos los elementos de un Set
clear_science_friends = science_friends
clear_science_friends.clear()
print("4.4: ", clear_science_friends)

#Operaciones Avanzadas de los Sets
art_friends2 = {"Rolf", "Anne", "Jen"}
science_friends2 = {"Jen", "Charlie"}

# 6.Difference quita los elementos que son comunes del primer Set con el segundo Set y muestra el resultado
art_but_not_science = art_friends2.difference(science_friends2)
science_but_not_art = science_friends2.difference(art_friends2)
print("6.1: ", art_but_not_science)
print("6.2: ", science_but_not_art)

# 7.Symmetric_difference obtiene los elementos que no son comunes en ambos Sets
not_in_both = art_friends2.symmetric_difference(science_friends2)
print("7: ", not_in_both)

# 8.Intersection obtiene los elementos que son comunes en ambos Sets 
art_and_science = art_friends2.intersection(science_friends2)
print("8: ", art_and_science)

# 9.Union combina todos los elementos de ambos Sets
all_friends = art_friends2.union(science_friends2)
print("9: ", all_friends)

# 10.Declarando un Set vacío
empty_set = set()
print("10: ", empty_set)

# 11.Puedo combinar un set con otra collección, utilizando las operaciones avanzadas de los Sets
letters = {"a", "b", "c"}
numbers = [1, 2, 3]
letters_and_numbers = letters.union(numbers)
print("11: ", letters_and_numbers)

# 12.Puedo revisar si un elemento existe en un Set utilizando in
#Este método lo puedo aplicar para strings, dictionarios y cualquier otra colección de datos
print("12.1: ", "a" in letters)
print("12.2: ", 4 in numbers)

#EJERCICIOS
#E1)
my_set = set()
print("E1: ", my_set)

#E2)
my_set.add("Executioner")
my_set.update(["Racardo", "Python"])
print("E2: ", my_set)

#E3)
my_ricardos = {"Ricardo", "Rocardo", "Racardo"}
print("E3: ", my_ricardos)

#E4)
my_set_union_ricardos = my_set.union(my_ricardos)
my_set_sdifference_ricardos = my_set.symmetric_difference(my_ricardos)
my_set_intersection_ricardos = my_set.intersection(my_ricardos)
print("E4: ",my_set_union_ricardos, my_set_sdifference_ricardos, my_set_intersection_ricardos)

#E5)
number_range = range(1,11)
my_numbers = set()
my_numbers.update(number_range) #En vez del for de abajo, puedo utilizar update
"""for n in number_range:
    my_numbers.add(n)"""

user_number = int(input("Enter a integer number: "))

if user_number in my_numbers:
    print(f"Congratulations your number ({user_number}) is in the range 1-10")
elif user_number < 1:
    print(f"Soory your number {user_number} is too low")
else:
    print(f"Sorry your number {user_number} is too high")

