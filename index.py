import tkinter as tk
from tkinter import messagebox
import pygame

def mostrar_mensagem():
    janela_mensagem = tk.Toplevel(janela)
    janela_mensagem.title("Mensagem de Apresentação")

    label = tk.Label(janela_mensagem, text="Quer me conhecer melhor?")
    label.pack(padx=20, pady=10)

    # Função para lidar com o botão "Sim"
    def sim():
        janela_mensagem.destroy()
        exibir_mensagem()

    # Função para lidar com o botão "Não"
    def nao_confirmacao():
        janela_confirmacao = tk.Toplevel(janela)
        janela_confirmacao.title("Confirmação")

        label_confirmacao = tk.Label(janela_confirmacao, text="Tem certeza?")
        label_confirmacao.pack(padx=20, pady=10)

        # Função para lidar com o botão "Sim" na confirmação
        def sim_confirmacao():
            janela_confirmacao.destroy()
            janela_mensagem.destroy()
            auto_destruicao()

        # Função para lidar com o botão "Não" na confirmação
        def nao_confirmacao():
            janela_confirmacao.destroy()

        # Botões "Sim" e "Não" na confirmação
        botao_sim_confirmacao = tk.Button(janela_confirmacao, text="Sim", command=sim_confirmacao)
        botao_sim_confirmacao.pack(pady=5)
        botao_nao_confirmacao = tk.Button(janela_confirmacao, text="Não", command=nao_confirmacao)
        botao_nao_confirmacao.pack(pady=5)

    # Botões "Sim" e "Não" na mensagem principal
    botao_sim = tk.Button(janela_mensagem, text="Sim", command=sim)
    botao_sim.pack(pady=5)
    botao_nao = tk.Button(janela_mensagem, text="Não", command=nao_confirmacao)
    botao_nao.pack(pady=5)

def auto_destruicao():
    janela_contagem = tk.Toplevel(janela)
    janela_contagem.title("Auto destruição")

    label_contagem = tk.Label(janela_contagem, text="Auto destruição em 10 segundos")
    label_contagem.pack(padx=20, pady=10)

    # Inicialização do pygame e carregamento da música
    pygame.mixer.init()
    pygame.mixer.music.load("bomba.mp3")

    contador = 10

    # Função para reproduzir a música
    def reproduzir_musica():
        pygame.mixer.music.play()

    # Função para atualizar a contagem regressiva
    def atualizar_contagem():
        nonlocal contador
        if contador >= 0:
            label_contagem.config(text=f"Auto destruição em {contador} segundos")
            contador -= 1
            janela_contagem.after(1000, atualizar_contagem)
        else:
            # Parar a reprodução da música e fechar a janela de contagem
            pygame.mixer.music.stop()
            janela_contagem.destroy()
            messagebox.showinfo("Resposta", "Caiu na pegadinha.")

    # Reproduzir a música e iniciar a contagem regressiva
    reproduzir_musica()
    atualizar_contagem()

def exibir_mensagem():
    messagebox.showinfo("Mensagem", "Então, bora conversar!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Janela Principal")

# Criando um botão para exibir a mensagem
botao = tk.Button(janela, text="Clique aqui pela curiosidade", command=mostrar_mensagem)
botao.pack(padx=50, pady=20)

# Iniciando o loop principal da janela
janela.mainloop()
