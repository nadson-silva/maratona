import tkinter as tk
import problema_01

global backgound_color
backgound_color = '#5555FC'


def toDo():
    return 'teste'


def menuWindow():
    menu.tkraise()


def cesarWindow():
    print('01')
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

    # texto_code = tk.Entry(cesarFrame, width=100)
    # texto_code.grid(column=0, row=2)

    # texto_code1 = tk.Entry(cesarFrame, width=100)
    # texto_code1.grid(column=0, row=6)

    encode_button = tk.Button(cesarFrame, text="Codificar Mensagem",
                              command=lambda: problema_01.encode(text_entry.get().upper(), key_entry.get(), output_label))
    encode_button.place(relx=0.15, rely=0.45, relwidth=0.3)

    decode_button = tk.Button(cesarFrame, text="Decodificar Mensagem",
                              command=lambda: problema_01.decode(text_entry.get().upper(), key_entry.get(), output_label))
    decode_button.place(relx=0.55, rely=0.45, relwidth=0.3)

    output_label = tk.Label(cesarFrame)
    output_label.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.2)

    menu_button = tk.Button(cesarFrame, text='Menu', command=menuWindow)
    menu_button.place(relx=0.1, rely=0.9, relwidth=0.1)

    # saida1 = tk.Label(cesarFrame, text='')
    # saida1.grid(column=0, row=3)

    # saida2 = tk.Label(cesarFrame, text='')
    # saida2.grid(column=0, row=7)

    # label_title = tk.Label(cesarFrame, text='Cifra de Céasar').pack()

    cesarFrame.tkraise()


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
    menu, text='Cifra de Vigenère II', command=lambda: toDo)
cifra_vigenere.place(relwidth=0.35, height=50, relx=0.325, rely=0.55)

cerca_trilho = tk.Button(menu, text='Cerca de Trilho', command=lambda: toDo)
cerca_trilho.place(relwidth=0.35, height=50, relx=0.325, rely=0.85)


menu.tkraise()
root.mainloop()
