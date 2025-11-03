from flask import Flask, jsonify
import time
import logging
import socket

app = Flask(__name__)

start_time = time.time()
request_count = 0

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

@app.route('/')
def index():
    global request_count
    request_count += 1
    logging.info("Main route accessed")
    return "Сервіс працює"

def send_to_statsd(message):
    """Send error message to UDP StatsD server"""
    UDP_IP = "127.0.0.1"
    UDP_PORT = 9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

@app.route('/error')
def error():
    global request_count
    request_count += 1
    try:
        1 / 0  # викликаємо помилку
    except Exception as e:
        logging.exception("An error occurred!")
        send_to_statsd(f"Error occurred: {str(e)}")
        return "Помилка оброблена. Перевірте логи.", 500
