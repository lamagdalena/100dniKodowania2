your_numbers = input("Input your numbers, separated by a comma: ")
lista_liczb = your_numbers.replace(" ", "").split(",")
krotki = tuple(lista_liczb)

print(lista_liczb)
print(krotki)