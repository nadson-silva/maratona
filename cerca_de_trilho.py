import numpy as np

char = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

text = input('texto').upper()
key = input('key')

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
            matriz = [ colunas ]*(linhas)
    else:
        colunas = [""]*7
        linhas = len(text) // 7 + 1
        matriz = [ colunas ]*(linhas)

    cont_l = 0
    matriz_tuple = [""]*linhas
    lista_chave = [0]*len(key)
    cont = -1

    pular_prox = 0

    for i in key:
        cont += 1
        lista_chave[cont] = i

    for cont_linha in range(0, linhas):
        for cont_coluna in range(0, 7) :
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
            
    

def encode(text, key):
    if textValidation(text, key):
        
        matriz_tuple = gerarMatriz(text, key)
        
        print(matriz_tuple)
    
        text_encoded = ''
        key_array = []
        key_array_int = []
        
        for i in key:
            key_array.append(i)
            key_array_int.append(i)
            
        key_array_int.sort()
        print(key_array)
        
        for j in key_array_int:
            pos = key_array.index(str(j))
            for i in range(len(matriz_tuple)):
                if matriz_tuple[i][pos] is not None:
                    text_encoded += matriz_tuple[i][pos]

        print(text_encoded)
        decode(text_encoded, key)


def decode(text, key):
    if textValidation(text, key):
        matriz_tuple = gerarMatriz(text, key)
        
        print(matriz_tuple)
        
        matriz_tuple = np.array(matriz_tuple).reshape(7, -1)
        
        print(matriz_tuple)
        
        # for row in matriz_tuple:
        #     for element in row:
        
        text_encoded = ''
        key_array = []
        key_array_int = []
        
        for i in key:
            key_array.append(i)
            key_array_int.append(i)
            
            
        for j in key_array_int:
            pos = key_array.index(str(j))
            for i in range(len(matriz_tuple)):
                if matriz_tuple[i][pos] is not None:
                    text_encoded += matriz_tuple[i][pos]
        

        # for j in key_array_int:
        #     pos = key_array.index(str(j))
        #     for i in range(len(matriz_tuple)):
        #         if matriz_tuple[pos][i] is not None:
        #             text_encoded += matriz_tuple[pos][i]
        print(text_encoded)
        
        
    
decode(text, key)

# RP  OURODBEUOPOA