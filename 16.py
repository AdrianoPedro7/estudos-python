anos = int(input('Fuma a quantos anos?'))*365
quantidade = int(input('Quantos cigarros fuma por dia?'))*10/24
dias = anos*quantidade/24
print(f'Você teve {dias:.2f} a menos de vida')
