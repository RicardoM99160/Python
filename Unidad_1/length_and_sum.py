grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total/length
print(average)

#Si me hago la pregunta, ¿Cuál de las siguientes colecciones de datos
#es la más adecuada para almacenar notas?
grades1 = [80, 75, 90, 100] #La lista (arreglo) es la ideal
grades2 = (80, 75, 90, 100) #La tupla no es una buena idea, porque en teoría no la puedo "modificar"
grades3 = {80, 75, 90, 100} #El set es la peor opción porque no puedo tener notas repetidas

#Corto sobre diccionarios
lottery_numbers = {13, 21, 22, 5, 8}
players = [
    {
        'name': 'Ricardo',
        'numbers': {15, 21, 9, 22, 3}
    },
    {
        'name': 'Luca',
        'numbers': {5, 8, 13, 21, 9}
    }
]

for player in players:
    match = len(player['numbers'].intersection(lottery_numbers))
    print(f"Player {player['name']} got {match} numbers right")
