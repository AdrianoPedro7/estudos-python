import random
import string

def password_generator(len_pass = 8):
    num = string.digits
    stri = string.ascii_letters
    options = num+stri

    senha_user = ""
    for i in range(0, len_pass):
        digit = random.choice(options)
        senha_user = senha_user+digit

    return senha_user

choice_user = input('Você quer a senha com quantos digitos? ')

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print('Entrada invalida')
    quit()
response = password_generator(len_pass = choice_user)
print(f'Senha Gerada: {response}')
enter = input('')