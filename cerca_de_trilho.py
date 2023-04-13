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

char = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def textValidation(text, key):
    for letter in text:
        if letter not in char:
            return False
    for letter in key:
        try:
            int(letter)
        except:
            return False
    if not len(set(key)) == 7:
        return False
    return True


def gerarMatriz(text, key):
    if (len(text) % 7) == 0:
        colunas = [""]*7
        linhas = len(text) // 7
        matriz = [colunas]*(linhas)
    else:
        colunas = [""]*7
        linhas = len(text) // 7 + 1
        matriz = [colunas]*(linhas)

    cont_l = 0
    matriz_tuple = [""]*linhas
    lista_chave = [0]*len(key)
    cont = -1

    pular_prox = 0

    for i in key:
        cont += 1
        lista_chave[cont] = i

    for cont_linha in range(0, linhas):
        for cont_coluna in range(0, 7):
            index = cont_coluna + pular_prox
            try:
                matriz[cont_linha][cont_coluna] = text[index]
            except:
                matriz[cont_linha][cont_coluna] = None
            if (cont_coluna == 6):
                cont_l += 1
                pular_prox += 7
            matriz_tuple[cont_linha] = tuple(matriz[cont_linha])

    return matriz_tuple


def encode(text, key, output):
    if textValidation(text, key):
        matriz_tuple = gerarMatriz(text, key)

        text_encoded = ''
        key_array = []
        key_array_sorted = []

        for i in key:
            key_array.append(i)
            key_array_sorted.append(i)

        key_array_sorted.sort()

        for j in key_array_sorted:
            pos = key_array.index(str(j))
            for i in range(len(matriz_tuple)):
                if matriz_tuple[i][pos] is not None:
                    text_encoded += matriz_tuple[i][pos]

        output.config(text=text_encoded, foreground="black")

        return True

    else:
        output.config(text='TEXTO OU CHAVE INVALIDA... TENTE NOVAMENTE!',
                      foreground="red")
        return False


def decode(text, key, output):
    if textValidation(text, key):
        text_array = []
        for letter in text:
            text_array.append(letter)

        key_array = []
        key_array_sorted = []

        for i in key:
            key_array.append(i)
            key_array_sorted.append(i)

        key_array_sorted.sort()

        if (len(text) % 7) == 0:
            colunas = [""]*7
            linhas = len(text) // 7
            matriz = [colunas]*(linhas)
        else:
            colunas = [""]*7
            linhas = len(text) // 7 + 1
            matriz = [colunas]*(linhas)

            for i in range(len(matriz)):
                matriz[i] = list(matriz[i])

            temp = ((len(text_array) % 7) - 7)
            for i in range(-1, temp - 1, -1):
                matriz[-1][i] = None

        for i in key_array_sorted:
            pos = key_array.index(str(i))
            for j in range(len(matriz)):
                if matriz[j][pos] != None:
                    matriz[j][pos] = text_array.pop(0)

        text_decoded = ''
        for i in matriz:
            for j in i:
                if j is not None:
                    text_decoded += j
        output.config(text=text_decoded, foreground="black")

        return True

    else:
        output.config(text='TEXTO OU CHAVE INVALIDA... TENTE NOVAMENTE!',
                      foreground="red")
        return False
