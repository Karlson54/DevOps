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
