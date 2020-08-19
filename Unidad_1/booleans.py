""" age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

my_number = 5
user_number = int(input("Enter a number: "))
matches = my_number == user_number
print(f"Yo got it right: {matches}.")

print(id(my_number))
print(id(age)) 

#Exercise 1
a = "culo"
b = "culo"
c = a

print(id(a))
print(id(b))
print(id(c))
print(a == b)
print(a is b)
print (a == c)
print(a is c) 

#Exercise 2
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
compare1 = numbers is new_numbers
id1 = id(numbers)
print(f"Numbers and new_numbers ar the same thing? {compare1}")

numbers = [1, 2, 3, 4]
numbers.append(5)
id2 = id(numbers)
compare2 = id1 == id2
print(f"Numbers is the same thing before apend 5? {compare2}")
print(id1)
print(id2) 

#Exercise 3
number = int(input("Enter a number: "))

if number > 0: 
    print(f"The number {number} is positive")
elif number < 0:
    print(f"The number {number} is negative")
else:
    print("Your number is equal to 0")  

#Exercise 4
hours_week = int(input("How many hours have you worked this week? "))
wage = int(input("Enter your hourly wage: $"))

if hours_week > 40:
    extra_hours = hours_week - 40
    extra_pay = extra_hours * wage * 1.10
    pay = (40 * wage) + extra_pay
    print(f"You have earned some additional pay: ${extra_pay}")
    print(f"This week you earn: ${pay}")
else:
    pay = hours_week * wage
    print(f"This week you earn: ${pay}")
"""

x = 35 and 0
y = 0 and 35
z = 45 or 0
k = 0 or 45
print(x,y,z,k)

a = True and False
b = False and True
c = True or False
d = False or True
print(a,b,c,d)

age = int(input("Enter your age: "))
usually_working = age >= 18 and age <= 65
print(f"At {age}, your usually working: {usually_working}")

name = input("Enter your name: ")
surname = input("Enter your surname: ")
greeting = name or f"Mr. {surname}"
print(greeting)