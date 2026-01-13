import traceback
import logging
import threading
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from pystray import Icon, MenuItem, Menu
from PIL import Image

from logic import importar_letra
from utils.resource_path import resource_path

# --- Configuração de logging ---
logging.basicConfig(
    filename="server_debug.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Abre a imagem
icon_image = Image.open(resource_path("icon.ico"))

# instanciar app Flask
app = Flask(__name__)
# configurar CORS
CORS(app)

# --- Funções para controlar o servidor ---
server_thread = None

def is_server_running():
    return server_thread is not None and server_thread.is_alive()

# criar rota para importar letras
@app.route('/import', methods=['POST'])
def importar():

  # obter dados JSON da requisição
  data = request.json
  
  try:
    # extrair URL da música
    url = data.get("url")

    # iniciar processo de importação
    importar_letra(url)

    return jsonify({ "status": "ok" })
  except Exception as e:

    # imprimir rastreamento de pilha para depuração
    traceback.print_exc()
    return jsonify({ "status": "error", "message": str(e) }), 500

# função para iniciar o servidor Flask em uma thread separada
def start_server():
    global server_thread
    if server_thread and server_thread.is_alive():
        logging.info("Servidor já rodando")
        return
    server_thread = threading.Thread(target=lambda: app.run(port=3000))
    server_thread.daemon = True
    server_thread.start()
    logging.info("Servidor iniciado")

    # Atualiza menu
    icon.update_menu()

# função para parar a aplicação
def kill_server(icon=None):
    # Nota: Flask não tem stop nativo, mas podemos fechar o app chamando sys.exit se quisermos parar tudo
    logging.info("Aplicativo fechado pelo usuário.")
    # Aqui, normalmente você só encerra a aplicação inteira ou sinaliza para threads
    os._exit(0) # opcional

# criar menu da bandeja
menu = Menu(
  MenuItem('Iniciar', start_server, enabled=lambda item: not is_server_running()),
  MenuItem('Sair', kill_server)
)

# criar ícone da bandeja
icon = Icon("Lyrics Importer", icon_image, "Lyrics Importer", menu)
  
# --- Inicia ícone da bandeja ---
icon.run()