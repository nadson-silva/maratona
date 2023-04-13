"""## Desafio 2"""

"""
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

####################################################


def char():
    return [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

####################################################


def matriz():
    char_m = char()
    linha_nada = [""]*37
    matriz_pree = [linha_nada]*37
    matriz_pree[0][0] = " "
    matriz_tuple = [""]*37

    matriz_pree[0] = char_m
    matriz_tuple[0] = char_m

    for i in range(1, 37, 1):
        j = 0
        for letter in matriz_pree[i-1]:
            index = char_m.index(letter) + 1
            while index > 36:
                index -= 37
            matriz_pree[i][j] = char_m[index]
            j += 1
        matriz_tuple[i] = tuple(matriz_pree[i])
    return matriz_tuple

####################################################


def encode(text, key, output):
    if not textValidation(text, key):
        output.config(text='TEXTO OU CHAVE INVALIDA... TENTE NOVAMENTE!',
                      foreground="red")
        return False
    matriz_cod = matriz()
    char_c = char()
    new_str_c = ''
    cont_c = -1
    for letter_text in text:
        cont_c += 1
        index_text = char_c.index(letter_text)
        index_key = char_c.index(key[cont_c])
        new_str_c = new_str_c + matriz_cod[index_key][index_text]

    output.config(text=new_str_c, foreground="black")
    return new_str_c

####################################################


def decode(text, key, output):
    if not textValidation(text, key):
        output.config(text='TEXTO OU CHAVE INVALIDA... TENTE NOVAMENTE!',
                      foreground="red")
        return False
    matriz_decod = matriz()
    char_d = char()
    new_str_d = ''
    cont_d = -1
    for letter_key in key:
        cont_d += 1
        index_key = char_d.index(letter_key)
        index_text = matriz_decod[index_key].index(text[cont_d])
        new_str_d = new_str_d + char_d[index_text]

    output.config(text=new_str_d, foreground="black")
    return new_str_d

####################################################


def textValidation(text, key):
    for letter in text:
        if letter not in char():
            return False
    for letter in key:
        if letter not in char():
            return False
    if not len(key) == len(text):
        return False
    return True
