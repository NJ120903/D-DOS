# D-DOS

This repository contains two Python scripts for simulating a Distributed Denial of Service (DDoS) attack and for running a rate-limited server to test defenses against such attacks. 

## Overview

1. **Rate-Limited Server (`rate_limited_server.py`)**:
   - A simple Flask server with rate-limiting capabilities to handle and limit requests.
   - Designed to help test defensive measures against DDoS attacks.

2. **DDoS Simulation Script (`ddos_simulation.py`)**:
   - Simulates a DDoS attack by sending a large number of requests to a target server.
   - Allows specifying the number of requests and the number of concurrent threads.

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```
2. Install required packages:
   ```bash
   pip install flask requests
   ```

   ```bash
   python rate_limited_server.py
   ```
You will be prompted to enter the port number for the server. For example, enter 8080 to use port 8080.

# Running the DDoS Simulation
Run the DDoS simulation script:

```bash
python ddos_simulation.py
```
You will be prompted to enter:

The server URL (e.g., http://localhost:8080)
The total number of requests you want to send
The number of concurrent threads to use for sending requests
Example
Rate-Limited Server:

```yaml
Enter the port number for the server: 8080
DDoS Simulation Script:
```

Enter the server URL (e.g., http://YOUR_SERVER_IP:YOUR_SERVER_PORT): http://localhost:8080
Enter the total number of requests: 10
Enter the number of concurrent threads: 5

#Important Notes
Ethical and Legal Responsibility: Ensure you have explicit permission to perform such tests on the server. Unauthorized DDoS attacks are illegal and can result in severe legal consequences.
Server Load: Be cautious with the number of requests and concurrent threads. High values can easily crash the target server.
Educational Purpose: Use these scripts strictly for educational and defensive purposes to understand and mitigate DDoS attacks.

#Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.

   
