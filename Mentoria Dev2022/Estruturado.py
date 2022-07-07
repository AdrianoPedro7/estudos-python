input = input("Digite os números (1, 2, 3 ...): \n")

numbers = [int(numeros) for numeros in input.split(",")]
summation_even_numbers = 0

for number in numbers:
    if (number % 2 == 0):
        summation_even_numbers += number

print(f"Resultado: {summation_even_numbers}")






numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summation_even_numbers = 0

for number in numbers:
    if (number % 2 == 0):
        summation_even_numbers+= number

print(f"Resultado: {summation_even_numbers}")



num = 0
while(num < 10):
    print(num)
    num += 1



