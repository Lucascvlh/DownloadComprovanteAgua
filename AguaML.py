from pyautogui import typewrite
from pyautogui import click
from pyautogui import sleep
from pyautogui import hotkey
from pyautogui import press
from pyautogui import scroll
from PIL import ImageGrab
from tkinter import messagebox
import datetime
import inquirer

# Configuração de tela 1 de 1366 x 768
# Configuração de tela 2 de 1440 x 900
# Kirk em 90% de Zoom
# Deixar somente a aba do Kirk aberta

x = 0
y = 0
alturaLinha = 20
yPlanilha = 200 
contador = 0
print('Configurações para executar:\n Resolução da tela 1 em 1366 x 768 \n Resolução da tela 2 em 1440 x 900 \n Tela do Kirk em 90% \n Deixe somente a aba do Kirk aberta')
paraFazer = int(input('Quanto(s) chamado(s) para atender? '))

questions = [
  inquirer.List('Format',
                message="Qual o formato do arquivo",
                choices=['PDF', 'JPG', 'JPEG', 'PNG' ,'TXT'],
            ),
]
answers = inquirer.prompt(questions)

if answers['Format'] == 'TXT':
  while contador < paraFazer:
    click(1893,231)
    sleep(2)
    click(2664,283)
    scroll(-500)
    sleep(1)
    click(2214,743)
    sleep(1)
    typewrite('Arquivo inexistente.')
    click(2695,790)
    sleep(1)
    click(2439,142)
    sleep(1)
    typewrite('Arquivo inexistente.')
    sleep(1)
    click(2164,544)
    sleep(4)
    contador += 1
    print(str(datetime.datetime.now()))
if answers['Format'] != 'TXT':
  while contador < paraFazer:
    click(1893,231)
    sleep(2)
    click(2120, 528, clicks=2, interval=0.25)
    hotkey('ctrl','c')
    click(65,yPlanilha)
    hotkey('ctrl','shift','v')
    click(298,yPlanilha)
    sleep(0.25)
    typewrite('FL ')
    sleep(0.25)
    hotkey('ctrl','shift','v')
    sleep(2)
    press('down')
    press('enter')
    sleep(0.5)
    click(2114,261, clicks=2, interval=0.25)
    hotkey('ctrl','c')
    click(128,yPlanilha)
    hotkey('ctrl','shift','v')
    click(2143,654,clicks=3, interval=0.25)
    hotkey('ctrl','c')
    click(350,yPlanilha)
    hotkey('ctrl','shift','v')
    click(2137,655, clicks=2 ,interval=0.25)
    hotkey('ctrl','c')
    click(555,yPlanilha)
    hotkey('ctrl','shift','v')
    click(2168,655,clicks=2 ,interval=0.25)
    hotkey('ctrl','c')
    click(600,yPlanilha)
    hotkey('ctrl','shift','v')
    click(2146,589, clicks=2, interval=0.25)
    hotkey('ctrl','c')
    click(650,yPlanilha)
    hotkey('ctrl','shift','v')

    line1 = ImageGrab.grab(bbox=(690,200,820,212))
    checkPixelLine1 = line1.getpixel((x,y))
    line2 = ImageGrab.grab(bbox=(690,221,820,234))
    checkPixelLine2 = line2.getpixel((x,y))
    click(987,yPlanilha)

    typewrite('FATURA ARQUIVADA')
    sleep(2)
    press('down')
    press('enter')
    click(1058,yPlanilha)
    typewrite(str(datetime.date.today()))
    click(758,yPlanilha)
    hotkey('ctrl','c')
    click(2745,421)
    click(2713,772)
    if answers['Format'] == 'PDF':
      sleep(7)
      click(2692,95)
      sleep(3)
    elif answers['Format'] == 'JPG' or answers['Format'] == 'JPEG' or answers['Format'] == 'PNG':
      sleep(5)
      hotkey('ctrl','p')
      sleep(7)
      click(2440,692)
      sleep(2)
    if checkPixelLine1 == (244, 199, 195):
      messagebox.showwarning('Erro','Nomenclatura já usada.\nInsira a nomenclatura manualmente!')
      print('Saindo...')
      exit()
    elif checkPixelLine2 == (244, 199, 195):
      messagebox.showwarning('Erro','Nomenclatura já usada.\nInsira a nomenclatura manualmente!')
      print('Saindo...')
      exit()
    hotkey('ctrl','v')
    click(2394,506)
    sleep(1)
    click(1836,16)
    sleep(0.5)
    click(2346,144)
    sleep(0.5)
    if answers['Format'] == 'PDF':
      click(2163,466)
    elif answers['Format'] == 'JPG' or answers['Format'] == 'JPEG' or answers['Format'] == 'PNG':
      click(2161,492)
    yPlanilha += alturaLinha
    contador += 1
    if contador % 2 == 0:
      print(contador)
      print(contador % 2 == 0)
      click(65,yPlanilha)
      yPlanilha = 200
      scroll(-50) 
    sleep(4)
    print('Chamados: ' + str(contador) + ' - ' +str(datetime.datetime.now()))