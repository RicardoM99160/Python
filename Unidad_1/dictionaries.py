# 1.Los diccionarios se declaraun utilizando llaves. A diferencia de los Sets
#Los diccionarios si respetan el orden de los elementos y 
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print("1.1: ",friend_ages["Adam"])

#Esta es una manera de agregar elementos a un dictionary. Si la key no existe, inserta la nueva key con su respectivo
#value. En caso contrario solo actualiza el valor de la key que ya existe.
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print("1.2: ",friend_ages)

#Otra forma de modificar un dictionary es por medio de update
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}
meta_info = {
	"runtime": 181,
	"budget": "$356 million",
	"earnings": "$2.798 billion",
	"producer": "Kevin Feige"
}
movie.update(meta_info)
print("1.3: ", movie)

#Los diccionarios vienen siendo la implementación de los arreglos asociativos en python, accedo a los elementos utilizando
#sus key 
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 24},
    {"name": "Anne Pun", "age": 24},
)

print("1.4: ",friends[0]["name"])
print("1.5: ",friends[1]["name"])
print("1.6: ",friends[2]["name"])

# 2.Puedo convertir algunas colecciones de datos a diccionarios utilizando la función dict
friends2 = [("Ricardo", 21), ("Miltioxs", 22), ("Selvinator", 21), ("Rogers", 21), ("Cottiux", 21)]
friends2_ages = dict(friends2)
print("2: ",friends2_ages)

# 3.Con get puedo consultar dentro del dictionario si una key ya existe en él o no, sin causar un error
anime_dictionary = {
    "Name": "Naruto Shippuden",
    "Chapters": 600
}
print("3.1: ",anime_dictionary.get("Name"))
#Puedo especificar el valor devuelto por get en caso de no existir la llave que busco
print("3.2: ",anime_dictionary.get("Episodes", "No existe esta llave"))

# 4.Para eliminar un elemento de un diccionario, puedo utilizar en primer lugar del
movie2 = {
	"title": "Interestellar",
	"director": "Hans Zimmer",
	"year": 2020,
	"runtime": 180
}

del movie2["runtime"]
print("4.1: ",movie2)

#Además puedo utilizar el método pop, para eliminar un valor y obtenerlo
print("4.2: ","Elemento eliminado: "+movie2.pop("director"),movie2)

#Finalmente puedo utilizar clear para vaciar completamente un diccionario
movie2.clear()
print("4.3: ",movie2)

# 5.Iterar los elementos de un diccionario
#Por defecto obtengo las keys de los diccionarios
print("5.1: ---------------------------------------")
for attribute in movie:
	print(attribute)

#Para obtener los valores hago lo siguiente
print("5.2: ---------------------------------------")

"""for key in movie:
	print(movie[key]) #Esta forma es grotesca"""

for value in movie.values():
	print(value) #Esta forma es mejor

#Para obtener la key y su valor hago lo siguiente
print("5.3: ---------------------------------------")

"""for key in movie:
	print(f"{key}: {movie[key]}") #Esta forma es grotesca"""

for key, value in movie.items(): #items devuelve una tupla con cada par de key y value que tenga el diccionario
	print(f"{key}: {value}") #Esta forma es mejor

#Exercises

#1)
song_album_tuple = (
	"The Dark Side of the Moon",
	"Pink Floyd",
	1973,
	(
		"Speak to Me",
		"Breathe",
		"On the Run",
		"Time",
		"The Great Gig in the Sky",
		"Money",
		"Us and Them",
		"Any Colour You Like",
		"Brain Damage",
		"Eclipse"
	)
)
song_album = {}
song_album.update({
	"Name": song_album_tuple[0],
	"Artist": song_album_tuple[1],
	"Release year": song_album_tuple[2],
	"Track list": list(song_album_tuple[3])
})
print("E1: ",song_album)

#2)
print("E2: ---------------------------------------")
for key, value in song_album.items():
	print(f"{key}: {value}")

#3)
del song_album["Release year"]
song_album.pop("Track list")
song_album["Date of Release"] = "March 1st, 1973"
print("E3: ", song_album)

#4)
print("E4: ---------------------------------------")
print("Track List: ", song_album.get("Track list"))
#print("Track List: ", song_album["Track list"]) #Esto da error