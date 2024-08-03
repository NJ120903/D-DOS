import requests
import threading
import time
import random

# User inputs
url = input("Enter the server URL (e.g., http://YOUR_SERVER_IP:YOUR_SERVER_PORT): ")
number_of_requests = int(input("Enter the total number of requests: "))
concurrent_threads = int(input("Enter the number of concurrent threads: "))

# Counter to keep track of the number of requests sent
request_counter = 0
lock = threading.Lock()

def send_request():
    global request_counter
    while True:
        with lock:
            if request_counter >= number_of_requests:
                break
            request_counter += 1
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

threads = []
for _ in range(concurrent_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("DDoS simulation completed.")
