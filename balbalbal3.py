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

#print(matriz)


#cont_coluna = -1
cont_l = 0
pular_prox = 0
lista_chave = [0]*len(chave_e)
cont = -1

for i in chave_e:
    cont += 1
    lista_chave[cont] = i

for cont_linha in range(0, linhas + 1):
    for cont_coluna in range(0, 8) :
        matriz[cont_linha][cont_coluna + pular_prox] = palavra_e[cont_coluna + pular_prox]
        if (cont_coluna == 7):
            cont_l += 1
            pular_prox += 7

print(matriz)

