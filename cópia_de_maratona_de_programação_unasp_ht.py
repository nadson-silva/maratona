# -*- coding: utf-8 -*-
"""Cópia de Maratona de Programação Unasp-HT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LUt7kDduuz2UV65Px2EyRn91Jz1Avd42

##Desafio 1
"""

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

char = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

####################################################
def codificar(text, n):
    new_char = ''
    for letter in text:
        index = char.index(letter) + n
        if index > 36:
            while index > 36:
                index -= 37
        
        new_char = new_char + char[index]
    return new_char

####################################################
def decodificar(text, n):
    new_char = ''
    for letter in text:
        index = char.index(letter) - n
        if index < 0:
            while index < 0:
                index += 37
        
        new_char = new_char + char[index]
    return new_char

####################################################
print('-'*43)
print('|         Escolha uma das opções          |')
print('|         1 - Codificar Mensagem          |')
print('|         2 - Decodificar Mensagem        |')
print('-'*43)


option = 0

while option == 0:
    option = int(input('Digite a Opção escolhida: '))

    if option == 1:
        text = input('Digite um TEXTO para ser codificado:\n').upper()
        chave = int(input('Digite o NÚMERO da chave: '))
        print(codificar(text, chave))
    elif option == 2:
        text = input('Digite um TEXTO para ser decodificado:\n').upper()
        chave = int(input('Digite o NÚMERO da chave: '))
        print(decodificar(text, chave))
    else:
        print('NÚMERO INVÁLIDO. Veja novamente as opções')
        option = 0

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
  matriz_pree = [ linha_nada ]*37
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
def codificar_2(text, key):
    matriz_cod = matriz()
    char_c = char()
    new_str_c = ''
    cont_c = -1
    for letter_text in text:
      cont_c += 1
      index_text = char_c.index(letter_text)
      index_key = char_c.index(key[cont_c])
      new_str_c = new_str_c + matriz_cod[index_key][index_text]
      
    return new_str_c

####################################################
def decodificar_2(text_cod, key):
    matriz_decod = matriz()
    char_d = char()
    new_str_d = ''
    cont_d = -1
    for letter_key in key:
      cont_d += 1
      index_key = char_d.index(letter_key)
      index_text = matriz_decod[index_key].index(text_cod[cont_d])
      new_str_d = new_str_d + char_d[index_text]
    return new_str_d

####################################################

print('-'*43)
print('|         Escolha uma das opções          |')
print('|         1 - Codificar Mensagem          |')
print('|         2 - Decodificar Mensagem        |')
print('-'*43)


option = 0

while option == 0:
    option = int(input('Digite a Opção escolhida: '))

    if option == 1:
        texto = str(input('Digite um TEXTO para ser codificado:\n').upper())
        chave = str(input('Digite um TEXTO para a chave: ').upper())
        print('Resultado:\n', codificar_2(texto, chave))
    elif option == 2:
        texto = str(input('Digite um TEXTO para ser decodificado:\n').upper())
        chave = str(input('Digite o TEXTO da chave: ').upper())
        print('Resultado:\n', decodificar_2(texto, chave))
    else:
        print('NÚMERO INVÁLIDO. Veja novamente as opções')
        option = 0