def fat_iterativo(n):
    fat_iterativo = 1
    for i in range(1, n+1):
        fat_iterativo = fat_iterativo * i
    return fat_iterativo
print(fat_iterativo(100))

def fat_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fat_recursivo(n - 1)
print(fat_recursivo(100))