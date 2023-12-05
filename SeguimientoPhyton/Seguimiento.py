number = int(input("Ingrese un número: "))


if number % 2 == 0:
    print(f"{number} es un número par.")
else:
    print(f"{number} es un número impar.")


counter = 0


print("\nPrimeros 5 números pares:")
while counter < 5:
    print(number)
    number += 2  #
    counter += 1

