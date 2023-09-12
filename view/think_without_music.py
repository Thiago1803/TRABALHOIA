import os
from view.act_start_music import *
from view.act_talk_with_us import *

# Pasta do projeto com as musicas
pasta = "/home/thiago/Área de Trabalho/TRABALHOIA/musicas"



#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO NÃO ESTA TOCANDO NENHUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando
def menuSemMusica(textoEntendido):
    comando = textoEntendido[1].lower()
    
    if(comando not in "desligar"):
        # Busca uma determinada musica para reproduzi-la
        if(comando in "tocar"):
            textoEntendido = textoEntendido[2:] #ignora "papel" e "tocar" da lista, sobrando nome do cantor/banda e musica
            buscarMusica(textoEntendido)

        # Reproduz a playlist inteira
        elif(comando in "reproduzir"):
            reproduzirPlaylist()

        else:
            menuParaMensagens("Nao entendi o que você pediu, fale outra vez!")
    else:
        menuParaMensagens("Bom descanso, volte depois para fazermos outra festa!")



# Envia mensagens de erro ou de despedida para o robô falar
def menuParaMensagens(mensagem):
    falarMensagens(mensagem)



# Verifica se a pasta de musicas esta vazia
def verificarPlaylist(pasta):
    if not os.listdir(pasta):
        menuParaMensagens("Playlist sem músicas!")
        return -1
    
    return 1




def buscarMusica(nome):
    if verificarPlaylist(pasta) == 1:
        #Variavel de controle para indicar se a musica foi encontrada ou nao
        musicaIniciou = False

        # Percorre todos os arquivos na pasta, reproduzindo a musica desejada caso for encontrada
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            nome_arquivo, extensao= os.path.splitext(caminho_arquivo)

            # Transforma ambas strings em palavras com letras minusculas e compara se existe um arquivo com o nome informado
            if nome[0].lower() in nome_arquivo.lower():
                tocarMusica(caminho_arquivo)
                musicaIniciou = True
        
        if(musicaIniciou == False):
            menuParaMensagens("Música nao encontrada!")
        else:
            musicaIniciou = False
    


def reproduzirPlaylist():   
    if verificarPlaylist(pasta) == 1:
        # Percorre todos os arquivos na pasta, reproduzindo cada musica
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            tocarMusica(caminho_arquivo)
        