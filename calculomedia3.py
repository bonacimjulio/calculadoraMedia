import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def calcular_media_ponderada(prova, atividades):
    """Calcula a média ponderada considerando 60% da prova e 40% das atividades."""
    return round((prova * 0.6) + (atividades * 0.4), 1)

def verificar_aprovacao(media):
    """Verifica se o aluno foi aprovado com base na média."""
    if media > 5:
        return "Aprovado! :))"
    elif media == 5.0:
        return "Aprovado! \n                5 bola é 10 ^^"
    else:
        return "Reprovado :(("

def calcular_media():
    try:
        # Validação de dados: verificar se as notas estão entre 0 e 10
        prova = float(entry_prova.get())
        if prova < 0 or prova > 10:
            raise ValueError("Nota da prova deve estar entre 0 e 10.")

        atividades = float(entry_atividades.get())
        if atividades < 0 or atividades > 10:
            raise ValueError("Nota das atividades deve estar entre 0 e 10.")

        media = calcular_media_ponderada(prova, atividades)
        resultado = verificar_aprovacao(media)

        mensagem = f"Média: {media:.1f}\nSituação: {resultado}"
        messagebox.showinfo("Resultado", mensagem)

#messagebox.showerror("Erro",str(e)) como  alternativa
    except ValueError as e:
        messagebox.showerror("Erro", "Por favor, insira notas válidas ou '.' no lugar da ',' ")
        
# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Média")
janela.resizable(height = False, width = False)
janela.geometry('300x110')


# Carrega a imagem e redimensiona
backgroungImage = Image.open("imagens/logo-univesp_completo_cor-positivo.png")
# Obter as dimensões da janela
window_width = janela.winfo_screenwidth()
window_height = janela.winfo_screenheight()
# Redimensionar a imagem utilizando o filtro de resampling (BICUBIC)
size = (window_width, window_height)
image_backgroungImage = backgroungImage.resize(size, resample=Image.BICUBIC)
photo = ImageTk.PhotoImage(backgroungImage)

# Widgets

# Cria um label e define a imagem como fundo
label_imagem_fundo = tk.Label(janela, image=photo)
label_imagem_fundo.place(x=0, y=0, relwidth=1, relheight=1)

label_atividades = tk.Label(janela, text="Nota Atividades:")
label_atividades.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

entry_atividades = tk.Entry(janela)
entry_atividades.grid(row=0, column=1, padx=10, pady=5)

label_prova = tk.Label(janela, text="Nota Prova:")
label_prova.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

entry_prova = tk.Entry(janela)
entry_prova.grid(row=1, column=1, padx=10, pady=5)

btn_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media)
btn_calcular.grid(row=2, column=1, columnspan=2, pady=10)

# Iniciar a aplicação
janela.mainloop()        