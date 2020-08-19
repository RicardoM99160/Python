cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

# 1. El break detiene un bucle repetitivo
print("1. Uso del break -----------------------------")
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"this car is {status}.")

# 2. El continue ignora el código de restante de la iteración actual, y pasa a la siguiente
print("2. Uso de continue -----------------------------")
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue
    print(f"this car is {status}.")
    print("Shipping new car to customer!")

# 3. El else se ejecuta si dentro del for no se ha ejecutado ningun break o se producido algún error. Esto también aplica para el while

cars2 = ["ok", "ok", "ok", "ok", "ok", "ok"]

print("3. Uso de else -----------------------------")
for status in cars2:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"this car is {status}.")
    print("Shipping new car to a costumer")
else:
    print("All cars built successfully. No faulty cars!")