from time import sleep
from random import choice

with open('lista') as arquivo:
    linhas = arquivo.read()
    lista = linhas.split('\n')

palavra = choice(lista).upper()

acerto = erro = ''
palavra_certa = 0
cont = 6

print(f'Você tem {cont} chances pra acertar.')
while True:
    mensagem = ''
    for letra in palavra:
        if letra in acerto:
            mensagem += f'{letra} '
        else:
            mensagem += f'_ '
    print(mensagem)

    letra = str(input('Insira uma letra: ')).upper().strip()

    if letra in acerto+erro:
        print(f'Você ja tentou a letra {letra}!')
        continue
    if letra in palavra:
        acerto += letra
        palavra_certa += palavra.count(letra)
        if palavra_certa == len(palavra):
            print(f'Parabéns você acertou a palavra {palavra}')
            break
    if letra not in palavra:
        cont -= 1
        erro += letra
        print(f'Chances: {cont}')
        if cont <= 0:
            print(f'Você perdeu todas sua chances! A palavra era {palavra}')
            break
print('-' * 25, 'Fim!', '-' * 25)
