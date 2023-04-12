char = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def codificar(text):
    new_char = ''
    for letter in text:
        index = char.index(letter) + 3
        if index > 36:
            while index > 36:
                index -= 37
        
        new_char = new_char + char[index]
    print(new_char)

def decodificar(text):
    new_char = ''
    for letter in text:
        index = char.index(letter) - 3
        if index < 0:
            while index < 0:
                index += 37
        
        new_char = new_char + char[index]
    print(new_char)


print('-'*43)
print('|         Escolha uma das opções          |')
print('|         1 - Codificar Mensagem          |')
print('|         2 - Decodificar Mensagem        |')
print('-'*43)

option = input('Digite a Opção escolhida: ')

if option == 1:
    text = input('Digite um texto para ser codificado:').upper()
    codificar(text)
elif option == 2:
    text = input('Digite um texto para ser decodificado:').upper()
    decodificar(text)





