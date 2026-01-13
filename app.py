import traceback

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/import', methods=['POST'])
def importar():
  data = request.json
  
  try:
    url = data.get("url")
    return jsonify({ "status": "ok" })
  except Exception as e:
    traceback.print_exc()
    return jsonify({ "status": "error", "message": str(e) }), 500
  
if (__name__ == '__main__'):
  app.run(port=3000, debug=True)