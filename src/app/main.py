import traceback

from flask import Flask, request, jsonify
from flask_cors import CORS

from logic import importar_letra

# instanciar app Flask
app = Flask(__name__)
# configurar CORS
CORS(app)

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
  
# iniciar app Flask
if (__name__ == '__main__'):
  app.run(port=3000, debug=True)