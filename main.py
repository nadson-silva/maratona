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


import tkinter as tk
import cifra_de_cesar
import cifra_de_vegenere
import cerca_de_trilho
import clipboard

global backgound_color
backgound_color = '#5555FC'


def toDo():
    return 'teste'


def menuWindow():
    menu.tkraise()
    
def copy(text):
    clipboard.copy(text)
    


def cesarWindow():
    cesarFrame = tk.Frame(root, background=backgound_color)
    cesarFrame.place(relheight=1, relwidth=1)

    label_title = tk.Label(cesarFrame, text="CIFRA DE CESAR",
                           background=backgound_color, font=("Arial", 15))
    label_title.place(relwidth=0.9, height=50, relx=0.05, rely=0.05)

    text_label = tk.Label(cesarFrame, text='Insira sua mensagem:')
    text_label.place(relx=0.05, rely=0.2, relwidth=0.25)

    text_entry = tk.Entry(cesarFrame)
    text_entry.place(relx=0.35, rely=0.2, relwidth=0.5)

    key_label = tk.Label(cesarFrame, text='Insira a chave:')
    key_label.place(relx=0.05, rely=0.3, relwidth=0.25)

    key_entry = tk.Entry(cesarFrame)
    key_entry.place(relx=0.35, rely=0.3, relwidth=0.5)

    encode_button = tk.Button(cesarFrame, text="Codificar Mensagem",
                              command=lambda: cifra_de_cesar.encode(text_entry.get().upper(), key_entry.get(), output_label))
    encode_button.place(relx=0.15, rely=0.45, relwidth=0.3)

    decode_button = tk.Button(cesarFrame, text="Decodificar Mensagem",
                              command=lambda: cifra_de_cesar.decode(text_entry.get().upper(), key_entry.get(), output_label))
    decode_button.place(relx=0.55, rely=0.45, relwidth=0.3)

    output_label = tk.Label(cesarFrame, text='')
    output_label.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.2)
    
    copy_button = tk.Button(cesarFrame, text='Copiar', command=lambda: copy(output_label.cget('text')))
    copy_button.place(relx=0.45 , rely=0.8, relwidth=0.1)

    menu_button = tk.Button(cesarFrame, text='Menu', command=menuWindow)
    menu_button.place(relx=0.1, rely=0.9, relwidth=0.1)

    cesarFrame.tkraise()


def vigenereWindow():
    vigenereFrame = tk.Frame(root, background=backgound_color)
    vigenereFrame.place(relheight=1, relwidth=1)

    label_title = tk.Label(vigenereFrame, text="CIFRA DE VIGENÈRE",
                           background=backgound_color, font=("Arial", 15))
    label_title.place(relwidth=0.9, height=50, relx=0.05, rely=0.05)

    text_label = tk.Label(vigenereFrame, text='Insira sua mensagem:')
    text_label.place(relx=0.05, rely=0.2, relwidth=0.25)

    text_entry = tk.Entry(vigenereFrame)
    text_entry.place(relx=0.35, rely=0.2, relwidth=0.5)

    key_label = tk.Label(vigenereFrame, text='Insira a chave:')
    key_label.place(relx=0.05, rely=0.3, relwidth=0.25)

    key_entry = tk.Entry(vigenereFrame)
    key_entry.place(relx=0.35, rely=0.3, relwidth=0.5)

    encode_button = tk.Button(vigenereFrame, text="Codificar Mensagem",
                              command=lambda: cifra_de_vegenere.encode(text_entry.get().upper(), key_entry.get().upper(), output_label))
    encode_button.place(relx=0.15, rely=0.45, relwidth=0.3)

    decode_button = tk.Button(vigenereFrame, text="Decodificar Mensagem",
                              command=lambda: cifra_de_vegenere.decode(text_entry.get().upper(), key_entry.get().upper(), output_label))
    decode_button.place(relx=0.55, rely=0.45, relwidth=0.3) 

    output_label = tk.Label(vigenereFrame, text='')
    output_label.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.2)
    
    copy_button = tk.Button(vigenereFrame, text='Copiar', command=lambda: copy(output_label.cget('text')))
    copy_button.place(relx=0.45 , rely=0.8, relwidth=0.1)

    menu_button = tk.Button(vigenereFrame, text='Menu', command=menuWindow)
    menu_button.place(relx=0.1, rely=0.9, relwidth=0.1)

    vigenereFrame.tkraise()
    
def cercaDeTrilho():
    trilhoFrame = tk.Frame(root, background=backgound_color)
    trilhoFrame.place(relheight=1, relwidth=1)

    label_title = tk.Label(trilhoFrame, text="CERCA DE TRILHO",
                           background=backgound_color, font=("Arial", 15))
    label_title.place(relwidth=0.9, height=50, relx=0.05, rely=0.05)

    text_label = tk.Label(trilhoFrame, text='Insira sua mensagem:')
    text_label.place(relx=0.05, rely=0.2, relwidth=0.25)

    text_entry = tk.Entry(trilhoFrame)
    text_entry.place(relx=0.35, rely=0.2, relwidth=0.5)

    key_label = tk.Label(trilhoFrame, text='Insira a chave:')
    key_label.place(relx=0.05, rely=0.3, relwidth=0.25)

    key_entry = tk.Entry(trilhoFrame)
    key_entry.place(relx=0.35, rely=0.3, relwidth=0.5)

    encode_button = tk.Button(trilhoFrame, text="Codificar Mensagem",
                              command=lambda: cerca_de_trilho.encode(text_entry.get().upper(), key_entry.get().upper(), output_label))
    encode_button.place(relx=0.15, rely=0.45, relwidth=0.3)

    decode_button = tk.Button(trilhoFrame, text="Decodificar Mensagem",
                              command=lambda: cerca_de_trilho.decode(text_entry.get().upper(), key_entry.get().upper(), output_label))
    decode_button.place(relx=0.55, rely=0.45, relwidth=0.3) 

    output_label = tk.Label(trilhoFrame, text='')
    output_label.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.2)
    
    copy_button = tk.Button(trilhoFrame, text='Copiar', command=lambda: copy(output_label.cget('text')))
    copy_button.place(relx=0.45 , rely=0.8, relwidth=0.1)

    menu_button = tk.Button(trilhoFrame, text='Menu', command=menuWindow)
    menu_button.place(relx=0.1, rely=0.9, relwidth=0.1)

    trilhoFrame.tkraise()

# Main
root = tk.Tk()

root.title("Maratona de programação")
root.geometry('600x500')


menu = tk.Frame(root, background=backgound_color)
menu.place(relheight=1, relwidth=1)

label_title = tk.Label(
    menu, text='ESCOLHA UMA DAS OPÇÕES ABAIXO', background=backgound_color, font=("Arial", 15))
label_title.place(relwidth=0.9, height=50, relx=0.05, rely=0.05)

cifra_cesar = tk.Button(menu, text='Cifra de Céasar', command=cesarWindow)
cifra_cesar.place(relwidth=0.35, height=50, relx=0.325, rely=0.25)

cifra_vigenere = tk.Button(
    menu, text='Cifra de Vigenère II', command=vigenereWindow)
cifra_vigenere.place(relwidth=0.35, height=50, relx=0.325, rely=0.55)

cerca_trilho = tk.Button(menu, text='Cerca de Trilho', command=lambda: toDo)
cerca_trilho.place(relwidth=0.35, height=50, relx=0.325, rely=0.85)


menu.tkraise()
root.mainloop()
