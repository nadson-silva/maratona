palavra_e = input('Digite a palavra:\n')
chave_e = input('Digite os numeros para a chave:\n')

if (len(palavra_e) % 7) == 0:
    colunas = [""]*7
    linhas = len(palavra_e) // 7
    matriz = [ colunas ]*(linhas)
else:
    colunas = [""]*7
    linhas = len(palavra_e) // 7 + 1
    matriz = [ colunas ]*(linhas)

cont_l = 0
matriz_tuple = [""]*linhas
lista_chave = [0]*len(chave_e)
cont = -1

pular_prox = 0

for i in chave_e:
    cont += 1
    lista_chave[cont] = i

for cont_linha in range(0, linhas):
    for cont_coluna in range(0, 7) :
        index = cont_coluna + pular_prox
        matriz[cont_linha][cont_coluna] = palavra_e[index]
        if (cont_coluna == 6):
            cont_l += 1
            pular_prox += 7
        matriz_tuple[cont_linha] = tuple(matriz[cont_linha])

print(matriz_tuple)

