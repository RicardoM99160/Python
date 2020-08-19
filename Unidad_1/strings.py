##Strings

my_string = "Hello World!"

string_with_quotes = "Hello, its 'me.'"
another_with_quotes = "He said \"You are amazing\""

multiline = """Hello, world.

My name is Ricardo Majano. Welcome to my program"""

"""This is also a comment"""

name = "Ricardo"
greeting = "Hello " + name

age = 20
my_age = "I am " + str(age) + " years old"

##String Formating

name2 = "Hugo"
greeting2 = f"How are you, {name2}?"

name3 = "Hector"
final_greeting = "Hi, How are you {}?"
final_greeting2 = "{greeting}, How are you {name}?"
greeting3 = "Hallo"

name_greeting = final_greeting.format(name)
name2_greeting = final_greeting.format(name2)
name3_greeting = final_greeting2.format(greeting = greeting3, name = name3)

print(name_greeting)
print(name2_greeting)
print(name3_greeting)