'''
def fib(n):
    print(f'fib({n})')
    if n<= 2: return 1
    return fib(n-1) + fib(n-2)

print (fib(10))
def fat (n):
    if n <= 1: return 1
    return n * fat(n-1)


'''

dic = {}
def fib(n):
    if n <= 2: return 1
    if n not in dic:
        dic[n] = fib(n-1) + fib(n-2)
    return dic[n]
print (fib(10))

