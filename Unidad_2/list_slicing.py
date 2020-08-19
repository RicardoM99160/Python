
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jenn"]

print(friends[:4])
print(friends[:])
print(friends[-3:])
print(friends[:-2])
print(friends[-3:-1])

#Existe una clase slice, que cuenta con el siguiente constructor:
#slice(start,stop[, step])
#De igual manera se puede crear un slice utilizando la sintaxis [X:Y], donde X punto de inicio y Y punto de fin

slice_instance = slice(0,2)
print("Usando slice(0,2): ",friends[slice_instance])
print("Usando la sintaxis [0:2]: ",friends[0:2])

#En el slice siempre se ignora el elemento que se encuentre en la posicion final indicada
  
print("Se muestra desde Anna hasta Bob, excluyendo a Jenn: \n", friends[2:4])

#Puedo crear slices de tuplas, listas y cadenas. De los sets y diccionarios NO

s = slice(1,4)

t = (1,2,3,4,5)
l = [1,2,3,4,5]
c = "12345"

print("Slice de una Tupla: ",t[s])
print("Slice de una Lista: ",l[1:4])
print("Slice de una Cadena: ",c[s])

#Al dejar algunos valores vacios ocurre lo siguiente

print("Desde el inicio, hasta el 3er elemento: \n", friends[:4]) #Siempre se excluye el elemento en la posicion final
print("Desde el segundo elemento, hasta el último: \n", friends[2:]) #En este caso si se incluye el último elemento
print("Crea una nueva lista con todos los elementos: \n", friends[:])

#Puedo especificar un tercer parámetro en el slice correspondiente a los saltos (step) de elementos

print("Slice a saltos de 2: ", friends[0:5:2])
 