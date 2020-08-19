#Un for en python es más parecido a un foreach de otros lenguajes de programación

friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)

#El _ significa que los valores de elements me sirven para hacer tantas iteraciones como elementos tenga esa lista
#Y que no me interesa utilizar los valores almacenados en elements

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in elements:
    print("Hello World")

for index in range(10):
    print(index)

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}")

# Función range
# range establece un rango de números que siempre excluye al mayor numero especificado en la función
range(9) # me devuelve los valores del 0 al 8
range(5, 15) # me devuelve los valores del 5 al 14
range(1, 30, 3) # me devuelve los valores del 1 al 29 a saltos de 3
range(0, 10, -1) # si el range es imposible de lograr, la función devuelve una secuencia vacía

print(range(1,10)) # solo te muestra la definición del rango, no la sucesión de los números

#Exercises
#E1)

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    name = employee[0]
    pay = employee[1]*employee[2]
    print(f"{name} is due to be paid ${pay}")

#E2)
average_hwave = 0

for employee in employees:
    average_hwave = average_hwave + employee[2]/len(employees)

for employee in employees:
    if employee[2] > average_hwave:
        print(employee)
 