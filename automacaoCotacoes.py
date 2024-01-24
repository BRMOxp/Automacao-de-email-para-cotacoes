import yfinance 
import pyautogui
import pyperclip

#Inicializando variáveis

codigo = input("Digite o código da ação desejada: ")
email = input("Digite o email do destinatário: ")
dados = yfinance.Ticker(codigo).history("6mo")
fechamento = dados.Close
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]


#Automação

pyautogui.PAUSE = 2
#Abrir nova aba e e-mail
pyautogui.hotkey("ctrl","t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")
#Abrir função de escrever e-mail
pyautogui.click(x=84, y=193)
pyautogui.PAUSE = 0.25
pyperclip.copy(email)
pyautogui.hotkey("ctrl","v")
#Colocar assunto
pyautogui.hotkey("tab")
pyperclip.copy("Análises semestrais")
pyautogui.hotkey("ctrl","v")
#Colocar corpo do e-mail
pyautogui.hotkey("tab")
mensagem = f"""Prezado gestor,
Seguem as análises diárias dos últimos seis meses da ação {codigo}:
Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima,2)}
Cotação atual: R${round(atual,2)}

Qualquer dúvida, fico à disposição!
"""
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")
