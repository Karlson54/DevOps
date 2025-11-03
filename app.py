from flask import Flask, jsonify
import time
import logging
import socket

app = Flask(__name__)

start_time = time.time()
request_count = 0
