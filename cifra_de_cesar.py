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


def encode(text, key, output):
    if not textValidation(text):
        output.config(text='TEXTO INVALIDO... TENTE NOVAMENTE!',
                      foreground="red")
        return False
    try:
        key = int(key)
    except:
        output.config(text='CHAVE INVALIDA... TENTE NOVAMENTE!',
                      foreground="red")
        return False
    new_char = ''
    for letter in text:
        index = (char.index(letter) + key) % 37

        new_char = new_char + char[index]
    output.config(text=new_char, foreground="black")
    return True


def decode(text, key, output):
    if not textValidation(text):
        output.config(text='TEXTO INVALIDO... TENTE NOVAMENTE!',
                      foreground="red")
        return False
    try:
        key = int(key)
    except:
        output.config(text='CHAVE INVALIDA... TENTE NOVAMENTE!',
                      foreground="red")
    new_char = ''
    for letter in text:
        index = char.index(letter) - key
        while index < 0:
            index += 37
        new_char = new_char + char[index]
    output.config(text=new_char, foreground="black")
    return True
