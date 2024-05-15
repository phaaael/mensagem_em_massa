import pywhatkit as kit
import time

def ler_contatos(arquivo):
    with open(arquivo, 'r') as f:
        contatos = f.read().splitlines()
    return contatos

def ler_mensagem(arquivo):
    with open(arquivo, 'r') as f:
        mensagem = f.read()
    return mensagem

arquivo_contatos = 'contatos.txt'
arquivo_mensagem = 'mensagem.txt'

contatos = ler_contatos(arquivo_contatos)
mensagem = ler_mensagem(arquivo_mensagem)

def enviar_mensagem(contatos, mensagem):
    for contato in contatos:
        kit.sendwhatmsg(contato, mensagem, time.localtime().tm_hour, time.localtime().tm_min + 1, tab_close=False)
        time.sleep(20)

enviar_mensagem(contatos, mensagem)
