import time
import subprocess
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from datetime import datetime

# Configuración del bot de Telegram
TOKEN = 'TU_API_TOKEN'  # Sustituye por tu token de bot
CHAT_ID = 'TU_CHAT_ID'  # Sustituye por tu chat ID

# Función para obtener las llamadas perdidas usando ADB
def obtener_llamadas_perdidas():
    # Ejecutamos el comando ADB para obtener el historial de llamadas
    result = subprocess.run(["adb", "shell", "content", "query", "--uri", "content://call_log/calls", "--projection", "number,type,date"], capture_output=True, text=True)
    
    llamadas_perdidas = []
    if result.returncode == 0:
        # Separamos las líneas del resultado
        lines = result.stdout.splitlines()
        
        for line in lines:
            # Buscamos solo las llamadas perdidas (tipo 3 es una llamada perdida)
            if "type=3" in line:
                # Extraemos el número de teléfono y la fecha de la llamada
                number = line.split("number=")[1].split()[0]
                date = line.split("date=")[1].split()[0]
                # Convertimos el timestamp de la fecha a formato legible
                fecha_llamada = datetime.fromtimestamp(int(date) / 1000).strftime('%Y-%m-%d %H:%M:%S')
                llamadas_perdidas.append(f"Teléfono: {number}, Fecha: {fecha_llamada}")
    
    return llamadas_perdidas

# Función para enviar las llamadas perdidas a través de Telegram
def enviar_notificacion():
    llamadas = obtener_llamadas_perdidas()
    
    if llamadas:
        # Formateamos las llamadas perdidas para enviarlas en el mensaje
        mensaje = "¡Llamadas perdidas detectadas!\n\n"
        mensaje += "\n".join(llamadas)
    else:
        mensaje = "No hay llamadas perdidas recientes."

    # Conectamos con el bot de Telegram y enviamos el mensaje
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=mensaje)

# Función principal que se ejecutará continuamente
def main():
    # Configuramos el Updater y el dispatcher para el bot
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comando /start que el bot responderá al usuario
    def start(update, context):
        update.message.reply_text("Bot de notificación de llamadas perdidas iniciado.")
    
    dp.add_handler(CommandHandler("start", start))
    
    # Enviar notificación de llamadas perdidas cada 60 segundos (puedes ajustar el tiempo)
    while True:
        enviar_notificacion()  # Enviar las notificaciones de las llamadas perdidas
        time.sleep(60)  # Espera 1 minuto antes de volver a comprobar las llamadas

if __name__ == '__main__':
    main()
