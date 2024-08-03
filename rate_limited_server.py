from flask import Flask, request, jsonify
from collections import defaultdict
from time import time

app = Flask(__name__)
request_counts = defaultdict(list)
RATE_LIMIT = 5  # Max 5 requests per 10 seconds
WINDOW_SIZE = 10

@app.route('/')
def home():
    client_ip = request.remote_addr
    current_time = time()

    # Remove old request timestamps
    request_counts[client_ip] = [timestamp for timestamp in request_counts[client_ip] if current_time - timestamp < WINDOW_SIZE]

    if len(request_counts[client_ip]) >= RATE_LIMIT:
        return jsonify({"error": "Too many requests"}), 429

    request_counts[client_ip].append(current_time)
    return jsonify({"message": "Request successful"})

if __name__ == '__main__':
    port = int(input("Enter the port number for the server: "))
    app.run(host='0.0.0.0', port=port)
