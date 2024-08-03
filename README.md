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

   
