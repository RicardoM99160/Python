# 1.Mientras la condición del while es verdadera, las líneas de código que contiene se sigue ejecuntado
is_learning = True

while is_learning:
    print("You're learning")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"

user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")

# 2. continue keyword sirve para ignorar el resto del bucle repetitivo y saltar a la siguiente iteracion
i = 0
while i <= 10:
    if i % 2 != 0:
        i = i + 1
        continue
    print(i)
    i = i + 1

# 3. Puedo usar else con los bulces repetitivos. El else se ejecuta cuando en el bucle no hay ningun break que lo detenga

dividend = int(input("Please enter a number:"))
divisor = 2

while divisor < dividend:
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break
    divisor = divisor + 1
else:
    print(f"{dividend} is prime!")

#Exercises
# E1)

is_guessed = True
while is_guessed:
    user_number = int(input("Please enter a number between [0-100]: "))
    if user_number == 51:
        print(f"You have guessed the secret number {user_number}")
        is_guessed = False
    elif user_number <= 41:
        print("Your guess is too low")
    elif user_number > 41 and user_number < 51:
        print("Your guess is close but low")
    elif user_number > 51 and user_number < 61:
        print("Your guess is close but high")
    else:
        print("Your guess is too high")

# E2)
j = 0
magic_word = "Python"
while j < len(magic_word):
    if magic_word[j] == "o":
        j = j + 1
        continue
    print(magic_word[j])
    j = j + 1

# E3)
prime_number = 2
while prime_number <= 100:
    is_prime = True
    k = 2
    while k < prime_number:
        if prime_number % k == 0:
            is_prime = False
        k = k + 1
    if is_prime:
        print(prime_number)
    prime_number = prime_number + 1


    

