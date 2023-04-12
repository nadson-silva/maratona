""""
Equipe 04

Dário Lopes 13688 Eng. 9° Sem 
Gênesis Carvalho 061472 Eng. 9° Sem
Hillary Wogel 018680 Eng. 1° Sem
Leonardo Toledo 181773 Eng. 3° Sem
Melissa Mirella 184780 Eng. 3° Sem
Nadson de Souza 14380 Eng. 1º Sem
Quévelin Silva 180070 Eng. 3° Sem
Raúl Venâncio 173762 Eng. 3° Sem
Richard de Souza 199652 Sist. 1° Sem
Sabrina Medina 196739 Eng. 1° Sem

Data: 11/04/2023
"""

global char
char = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def textValidation(text):
    for letter in text:
        if letter not in char:
            return False
    return True


def encode(text, key):
    new_char = ''
    for letter in text:
        index = char.index(letter) + key
        if index > 36:
            while index > 36:
                index -= 37

        new_char = new_char + char[index]
    print(new_char)


def decode(text, key):
    new_char = ''
    for letter in text:
        index = char.index(letter) - key
        if index < 0:
            while index < 0:
                index += 37

        new_char = new_char + char[index]
    print(new_char)


while True:
    print('-'*43)
    print('|         Escolha uma das opções          |')
    print('|         1 - Codificar Mensagem          |')
    print('|         2 - Decodificar Mensagem        |')
    print('|         0 - Sair                        |')
    print('-'*43)

    option = input('Digite a Opção escolhida: ')

    if option == 1:
        text = input('Digite um texto para ser codificado:').upper()
        if textValidation(text):
            try:
                key = int(
                    input('Informe a chave numérica para codificar o texto: '))
                encode(text, key)
            except:
                print('A chave precisa ser um número inteiro')

        else:
            print('O texto inserido nâo segue o padrão esperado. Tente novamente!')
    elif option == 2:
        text = input('Digite um texto para ser decodificado:').upper()
        if textValidation(text):
            try:
                key = int(
                    input('Informe a chave numérica para codificar o texto: '))
                decode(text, key)
            except:
                print('A chave precisa ser um número inteiro')

        else:
            print('O texto inserido nâo segue o padrão esperado. Tente novamente!')

    elif option == 0:
        print("Bye")
        exit()
    else:
        print('Opção invalida. Tente novamente')
