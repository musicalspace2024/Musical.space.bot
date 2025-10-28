# main.py
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import logging

# Cargar variables de entorno desde .env
load_dotenv()

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Variables de entorno
API_KEY = os.getenv("API_KEY", "default_key")

@app.route("/")
def home():
    """Página principal"""
    logger.info("Ruta / visitada")
    return jsonify({
        "message": "Hola, mundo! 🚀",
        "api_key_actual": API_KEY
    })

@app.route("/sumar", methods=["POST"])
def sumar():
    """Suma dos números enviados en JSON"""
    data = request.get_json(force=True)
    try:
        a = float(data.get("a", 0))
        b = float(data.get("b", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Los valores deben ser números"}), 400
    resultado = a + b
    logger.info(f"Suma: {a} + {b} = {resultado}")
    return jsonify({"resultado": resultado})

@app.route("/multiplicar", methods=["POST"])
def multiplicar():
    """Multiplica dos números enviados en JSON"""
    data = request.get_json(force=True)
    try:
        a = float(data.get("a", 1))
        b = float(data.get("b", 1))
    except (TypeError, ValueError):
        return jsonify({"error": "Los valores deben ser números"}), 400
    resultado = a * b
    logger.info(f"Multiplicación: {a} * {b} = {resultado}")
    return jsonify({"resultado": resultado})

# Manejo de rutas inexistentes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Ruta no encontrada"}), 404

# Manejo de errores generales
@app.errorhandler(500)
def internal_error(e):
    logger.error(f"Error interno: {str(e)}")
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render asigna el puerto automáticamente
    logger.info(f"Iniciando servidor en puerto {port}")
    app.run(host="0.0.0.0", port=port)
