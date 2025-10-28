# main.py
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env (opcional)
load_dotenv()

app = Flask(__name__)

# Ejemplo de variable de entorno
API_KEY = os.getenv("API_KEY", "default_key")

@app.route("/")
def home():
    return jsonify({
        "message": "Hola, mundo!",
        "api_key_actual": API_KEY
    })

# Ejemplo de endpoint POST
@app.route("/sumar", methods=["POST"])
def sumar():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port)
