import pywhatkit as kit

import time
import pyautogui

def ler_contatos(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        contatos = f.read().splitlines()
    return contatos

def ler_mensagem(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        mensagem = f.read()
    return mensagem

def escrever_log(mensagem):
    with open('log_envio_mensagens.txt', 'a', encoding='utf-8') as f:
        f.write(mensagem + '\n')

def enviar_mensagem(contato, mensagem):
    if not contato.startswith('+'):
        contato = '+55' + contato

    try:
        kit.sendwhatmsg_instantly(contato, mensagem, wait_time=20, tab_close=False)
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.press('enter')
        log_msg = f'Mensagem enviada para {contato}'
        escrever_log(log_msg)
        print(log_msg)
    except Exception as e:
        log_msg = f'Falha ao enviar mensagem para {contato}: {e}'
        escrever_log(log_msg)
        print(log_msg)

arquivo_contatos = 'contatos.txt'
arquivo_mensagem = 'mensagem.txt'

contatos = ler_contatos(arquivo_contatos)
mensagem = ler_mensagem(arquivo_mensagem)

for contato in contatos:
    enviar_mensagem(contato, mensagem)
    time.sleep(10)

log_msg = f'Total de mensagens enviadas com sucesso: {len(contatos)}'
escrever_log(log_msg)
print(log_msg)
