import os
import threading
from flask import Flask
from highrise_bot_sdk import Bot, Event  # Ajusta según tu SDK

app = Flask(__name__)

# Ruta básica para saber que la app está viva
@app.route("/")
def home():
    return "Bot corriendo ✅"

# Función para ejecutar el bot
def run_bot():
    # Configura tu bot con tu token y lógica
    bot = Bot(token=os.environ.get("HIGHRISE_TOKEN"))  # Coloca tu token en las variables de entorno

    # Ejemplo de evento simple
    @bot.on(Event.MESSAGE_RECEIVED)
    def handle_message(message):
        print(f"Mensaje recibido: {message.content}")
        bot.send_message(message.user, "Hola, estoy activo!")

    # Ejecutar el bot (bucle infinito interno)
    bot.run()

if __name__ == "__main__":
    # Ejecutar el bot en un hilo separado para que Flask también funcione
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Puerto asignado por Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
