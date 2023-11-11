# Jogo da Forca - Versão 2
# Python 3.11.3 64-bit
# Criado por Victor Mattos

import os
import random
import unidecode

def clear_screen():
    # Limpar a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_word(type = 0):
    # Escolher a palavra
    # 0 - Aleatório
    # 1 - Nomes de Pessoas
    # 2 - Nomes de Frutas
    # 3 - Nomes de Países
    # 4 - Nomes de Animais

    file_name = [
        '',
        'Words/Names.txt',
        'Words/Fruits.txt',
        'Words/Country.txt',
        'Words/Animals.txt'
    ]

    if type == 0:
        type = random.randint(1, 4)

    type_name = None

    if type == 1:
        type_name = 'um Nome Próprio'
    elif type == 2:
        type_name = 'uma Fruta'
    elif type == 3:
        type_name = 'um País'
    else:
        type_name = 'um Animal'

    with open(file_name[type], 'r', encoding='UTF-8') as file:
        word = list(unidecode.unidecode(random.choice(list(file.readlines()))).upper())

    try:
        word.remove('\n')
    except:
        pass
    finally:
        return [type_name, word]
    

def game(content):
    # O jogo acontece aqui
    letters = []                            # Letras já digitadas
    word_size = 0                           # Tamanho da palavra (sem contar espaços e traços)
    ignored_char = [' ', '-']               # Caracteres que serão ignorados na palavra
    type_name, word = content               # Tipo da palavra e a lista contendo ela
    word_string = ''.join(word)             # Converte a lista com a palavra em um texto normal
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Alfabeto válido para o jogo

    for i in word:
        if not i in ignored_char:
            word_size += 1

    digit, win, tries, total = 0, word_size, word_size, 0

    while True:
        clear_screen()
        print(f'▸ A palavra é {type_name} com {word_size} letra(s). Boa sorte!')
        print('\n\nPalavra: ', end='')

        for letter in word:
            if letter in ignored_char:
                print(f'{letter} ', end='')
            else:
                if letter in letters:
                    print(f'{letter} ', end='')
                else:
                    print('_ ', end='')

        print(f'\n\n\n▸ Letras digitadas: {letters}')
        print(f'\n▸ Tentativas: {tries}') if tries > 1 else print(f'\n▸ Tentativas: {tries} [ÚLTIMA CHANCE, CUIDADO!]')
        
        digit = input('\n▸ Digite uma letra: ').upper()

        if digit == '':
            # Não digitou nada
            ...
        elif digit not in alphabet:
            # Verifica se a letra está no alfabeto
            input('\n\nPor favor, digite uma letra válida.')
        elif digit in letters:
            # Verifica se a letra já foi digitada antes
            input(f'\n\nA letra \'{digit}\' já foi digitada.')
        else:
            if digit in word:
                # Caso a letra esteja na palavra
                appeared = 0

                for letter in word:
                    if digit == letter:
                        win -= 1
                        appeared += 1
                
                input(f'\n\nMuito bem! A letra \'{digit}\' aparece {appeared} vez(es) na palavra.')
            else:
                # Caso a letra não esteja na palavra
                tries -= 1
                input(f'\n\nQue pena! A letra \'{digit}\' não aparece na palavra.')

            total += 1
            letters.append(digit)

            if win < 1:
                # Ganhou o jogo
                clear_screen()
                print(f'▸ A palavra era: {word_string}')
                print(f'\n\n▸ Tentativas: {total}')
                input('\n\n▸ Resultado: Você ganhou a partida. Parabéns!')
                break
            elif tries < 1:
                # Perdeu o jogo
                clear_screen()
                print(f'▸ A palavra era: {word_string}')
                print(f'\n\n▸ Tentativas: {total}')
                input('\n\n▸ Resultado: Você perdeu a partida. Tente novamente!')
                break
    

# Início do Programa
while True:
    clear_screen()
    print('Seja bem-vindo(a) ao Jogo da Forca.\n')

    print('\n▸ Escolha uma opção de palavras: ')
    print('\n\n1. Aleatório')
    print('\n2. Nomes de Pessoas')
    print('\n3. Nomes de Frutas')
    print('\n4. Nomes de Países')
    print('\n5. Nomes de Animais')
    print('\n0. Sair do Jogo')

    option = input('\n\n▸ Opção: ')

    match option:
        case '0':
            # Sair do Jogo
            print('\n▸ Obrigado por jogar!')
            break
        case '1':
            # Aleatório
            game(choose_word(type = 0))
        case '2':
            # Nomes de Pessoas
            game(choose_word(type = 1))
        case '3':
            # Nomes de Frutas
            game(choose_word(type = 2))
        case '4':
            # Nomes de Países
            game(choose_word(type = 3))
        case '5':
            # Nomes de Animais
            game(choose_word(type = 4))
        case _:
            # Outro caso
            input('\nPor favor, selecione uma opção válida.')

    