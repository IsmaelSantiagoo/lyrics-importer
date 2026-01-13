import time

import pyperclip
import pyautogui
import pygetwindow as gw

from utils.fetch import fetch_lyrics
from utils.formatter import format_for_projection

from pathlib import Path

# caminho para recursos
BASE_DIR = Path(__file__).parent 

# caminho para imagem do botão importar
IMG_IMPORTAR = BASE_DIR / "resources" / "importar_btn.png"

# função para importar letra no ProPresenter
def importar_letra(url):
    
    # buscar letra e formatar
    raw = fetch_lyrics(url)
    formatted = format_for_projection(raw, 2)

    # copiar para área de transferência
    pyperclip.copy(formatted)
    time.sleep(0.2)

    # focar ProPresenter
    focar_propresenter()

    # aciona o atalho de importação da área de transferência
    acionar_atalho_importacao()

    # confirmar sobrescrição (se necessário)
    time.sleep(0.3)
    pyautogui.press("enter") 

# função para focar janela do ProPresenter
def focar_propresenter():
    
    # obter janela do ProPresenter
    windows = gw.getWindowsWithTitle("ProPresenter")

    # verificar se a janela foi encontrada
    if not windows:
        raise Exception("ProPresenter não está aberto")

    # focar janela
    win = windows[0]

    # restaurar se minimizada
    if win.isMinimized:
        win.restore()
        time.sleep(0.3)

    # clique dentro da janela para focar
    x = win.left + 500
    y = win.top + 20

    pyautogui.click(x, y)
    time.sleep(0.3)

def acionar_atalho_importacao(): 

    # abrir importação da área de transferência
    pyautogui.hotkey("ctrl", "shift", "u")
    time.sleep(0.5)

    # localizar botão importar
    btn = pyautogui.locateCenterOnScreen( str(IMG_IMPORTAR), confidence=0.85, grayscale=True)
    time.sleep(0.3)

    # confirmar importação
    pyautogui.press("enter") 
    
    # clicar no botão se encontrado
    if btn: 
        pyautogui.click(btn) 
        return True
    return False