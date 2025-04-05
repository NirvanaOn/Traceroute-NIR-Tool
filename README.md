# Traceroute-NIR-Tool

Traceroute OS Detection and Geo-location Tool

This Python-based tool enhances traditional traceroute functionality with OS detection, geo-location lookup, RTT spike detection, and private IP address detection. It's designed for network administrators, security professionals, or anyone interested in understanding their network's path and detecting potential anomalies.

---

## 🚀 Key Features

### 1. **Traceroute Functionality**
- Tracks the hops between your machine and the target IP or domain.
- Provides hop details like IP address, RTT (Round-Trip Time), and TTL value.

### 2. **Operating System (OS) Detection**
- Detects the OS of each hop based on TTL values:
  - Linux/Unix: TTL ≤ 64
  - Windows: TTL ≤ 128
  - Cisco/Networking Devices: TTL ≤ 255

### 3. **Geo-location Lookup**
- Retrieves the country, city, latitude, and longitude of each IP address along the route.

### 4. **RTT Spike Detection**
- Flags significant increases in RTT between consecutive hops to identify potential network issues.

### 5. **Private IP Detection**
- Detects private IP addresses in a public traceroute, indicating network misconfigurations.

### 6. **Logging**
- Logs the traceroute results (IP, RTT, TTL, OS, Location) to a file for troubleshooting and network analysis.

---

## 🧑‍💻 How It Works

1. **ICMP Echo Request Packets**: The tool sends ICMP Echo Requests with increasing TTL values to trace the network route.
2. **OS Detection**: Based on TTL values, the tool guesses the OS of each hop.
3. **Geo-location Lookup**: Uses ip-api to fetch the physical location of each IP.
4. **RTT Monitoring**: Identifies RTT spikes that indicate network problems.
5. **Private IP Detection**: Flags private IP addresses that should not be seen in a public traceroute.

---

## 📦 Prerequisites

- Python 3.x or higher
- **Scapy**: For crafting and sending ICMP packets.
- **Requests**: To fetch geo-location data.

To install the dependencies, run:

```bash
pip install -r requirements.txt

```bash
python .py


