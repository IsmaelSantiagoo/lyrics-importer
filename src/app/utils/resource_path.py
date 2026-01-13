import sys
from pathlib import Path

def resource_path(relative_path):
    """Retorna o caminho correto para recursos, seja rodando no Python ou em .exe"""
    if getattr(sys, 'frozen', False):
        # PyInstaller extrai arquivos para pasta temporária _MEIPASS
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent.parent
    return base_path / relative_path