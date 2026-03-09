# lista är en samling av värden
numbers = [1, 2, 3, 4, 5]  # innehåller alla dessa som separata objekt
# Vi kan komma åt objekten med hakparenteser

# listor är nollindexerade
print(numbers[0])

# vi kan få ut sista värdet med dessa
print(numbers[len(numbers) - 1])
print(numbers[-1])

# För att loopa använder vi keyword for
for i in range(1, 10):
    print(i)


# för att automatiskt loopa över alla värden i en lista använder vi ordet in
for number in numbers:
    print(number)


# om vi vill ha index ur listan använder vi enumerate
for index, number in enumerate(numbers):
    print(index, number)

numbers = [1, 2, 3, 4, 5, 6]


# att ta bort saker ur en lista kan vara problematiskt
for index, number in enumerate(numbers):
    numbers.pop(index)

print(numbers)
