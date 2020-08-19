friend = "Rolf"
user_name = input("Enter your name: ")

# 1.Para los if es importante que el código que le sigue esté indentado por espacios para que se encuentren
# esas líneas de código dentro del alcance del if

if user_name == friend:
    print("1.1: ","Hello, friend!")
    print("1.2: ","This runs too.")
else:
    print("1.3: ","Hello, stranger!")

print("1.4: ","This runs anyway.")
    #print("This will give me an error")

# 2.Con la función bool puedo saber si determinados valores son verdaderos o falsos
print("2.1: ", bool(5))
print("2.2: ", bool(0))

name = input("Enter your name: ")
if name:
    print("2.3: ", "We know your name.")

# 3. Con in puedo revisar si un valor se encuentra dentro de una lista (arreglo)
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name2 = input ("Enter your name: ")

if user_name2 in friends:
    print("3.1: ", "Hello, friend!")
elif user_name2 in family:
    print("3.2: ", "Hello, family!")
else:
    print("3.3: ", "I dont know you.")

# 4. Ternary operator (Forma resumida del if)
# syntax: <value if condition True> if <condition> else <value if condition False>

x = 6
value1 = x if x < 10 else "Invalid value"
value2 = x if x > 10 else "Invalid value"
print("4.1: ", value1)
print("4.2: ", value2)