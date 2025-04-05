Traceroute-NIR-Tool

Traceroute OS Detection and Geo-location Tool
This Python-based tool implements a Traceroute functionality with enhanced capabilities to detect the operating system (OS) of network hops, perform geo-location lookup of IP addresses, and detect RTT spikes and private IP addresses in a public trace. It utilizes ICMP Echo Request packets with varying TTL (Time-to-Live) values to trace the route to a target IP or domain. This tool can be particularly useful for network administrators, security professionals, and anyone interested in understanding the network route and detecting anomalies in the path.

Key Features:
Traceroute Functionality:

Tracks the hops (intermediate routers) between your machine and the target.

Provides detailed information about each hop, such as the IP address, round-trip time (RTT), and TTL value.

Operating System (OS) Detection:

Attempts to identify the operating system (OS) of each hop based on the TTL value in the ICMP response. The OS is guessed according to typical default TTL values for different OS types:

Linux/Unix: TTL ≤ 64

Windows: TTL ≤ 128

Cisco/Networking Device: TTL ≤ 255

This OS detection can help identify network devices and routers in the path.

Geo-location Lookup:

For each hop, the tool retrieves the country, city, latitude, and longitude of the IP address using the ip-api service.

This helps visualize the physical location of the hops along the route.

RTT Spike Detection:

Detects significant increases in Round-Trip Time (RTT) between consecutive hops. A sudden spike in RTT could indicate network congestion or an issue with a particular hop.

If the RTT exceeds 3 times the previous RTT, the tool flags this as an anomaly.

Private IP Detection:

Identifies if a private IP address (e.g., from a private subnet like 10.x.x.x, 172.16.x.x, or 192.168.x.x) appears in a public traceroute. This can indicate a misconfiguration or an unexpected response from a private network.

Logging:

Logs the output of each traceroute session to a text file, including detailed hop information, RTT values, TTLs, and OS detection results.

Logs can be reviewed for troubleshooting or analyzing network behavior over time.

Customizable Parameters:

The tool allows you to customize the maximum number of hops for traceroute (max_hops) and set a timeout for each hop response.

The program supports any valid IP address or domain name as a target.

Output Example:
yaml
Copy code
Tracing route to 8.8.8.8...

Hop 1 : 192.168.1.1 || RTT : 92.61ms || TTL = 64 || OS Detected : Linux/Unix || Location Found : (Unknown, Unknown, 0, 0) || TTL Normal
Hop 2 : No Reply
Hop 3 : 10.244.11.1 || RTT : 55.71ms || TTL = 62 || OS Detected : Linux/Unix || Location Found : (Unknown, Unknown, 0, 0) || Private IP in public trace
Hop 4 : 52.95.67.33 || RTT : 80.07ms || TTL = 248 || OS Detected : Cisco/Networking Device || Location Found : (India, Mumbai, 19.076, 72.8777) || TTL Normal
...
Destination Reached
OS of Destination : Cisco/Networking Device
How It Works:
ICMP Packet Sending:

The tool sends ICMP Echo Request packets with increasing TTL values (starting from 1).

Each hop along the network path decrements the TTL by 1 until the packet reaches the destination.

The tool listens for ICMP Echo Reply packets to calculate the RTT for each hop and determines the TTL value returned by each hop.

OS Detection Based on TTL:

Each hop's TTL value helps determine the most likely operating system. For example, Linux devices often have a TTL of 64, while Windows devices usually have a TTL of 128.

This OS detection is based on well-known default TTL values for various operating systems and network devices.

Geo-location Lookup:

The tool queries the ip-api API for each IP address encountered during the traceroute.

It retrieves the physical location (country, city, latitude, longitude) of the IP address. If the lookup fails, it returns "Unknown" as the location.

Anomaly Detection:

The tool monitors the RTT for each hop and detects sudden spikes (e.g., if the RTT of a hop is more than three times the previous hop's RTT).

It flags private IP addresses in the traceroute response, which shouldn't be visible in a public trace, suggesting potential network configuration issues.

Logging and Output:

Detailed information about each hop, including the IP address, RTT, TTL, OS, location, and any detected anomalies, is logged in a file (Traceroute_logs.txt).

The tool prints the traceroute results to the console in real-time and logs them for future reference.

Prerequisites:
Python 3.x or above

Scapy library for crafting and sending ICMP packets.

Requests library for making HTTP requests to retrieve geo-location data.

To install the dependencies, run:

bash
Copy code
pip install -r requirements.txt
How to Use:
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/traceroute-os-detection.git
cd traceroute-os-detection
Run the script:

bash
Copy code
python traceroute_os_detection.py
Enter a target IP or domain when prompted:

bash
Copy code
Enter IP or Domain : 8.8.8.8
The tool will perform the traceroute, display detailed results for each hop, and log the output to a file (Traceroute_logs.txt).

Example Output:
yaml
Copy code
Tracing route to 8.8.8.8...

Hop 1 : 192.168.1.1 || RTT : 92.61ms || TTL = 64 || OS Detected : Linux/Unix || Location Found : (Unknown, Unknown, 0, 0) || TTL Normal
Hop 2 : No Reply
Hop 3 : 10.244.11.1 || RTT : 55.71ms || TTL = 62 || OS Detected : Linux/Unix || Location Found : (Unknown, Unknown, 0, 0) || Private IP in public trace
Hop 4 : 52.95.67.33 || RTT : 80.07ms || TTL = 248 || OS Detected : Cisco/Networking Device || Location Found : (India, Mumbai, 19.076, 72.8777) || TTL Normal
...
Destination Reached
OS of Destination : Cisco/Networking Device
Contribution:
Feel free to fork the repository and submit pull requests. Contributions are welcome for:

Improving the OS detection algorithm.

Adding additional features such as more advanced anomaly detection or integration with different geo-location services.

Improving the UI/UX for displaying traceroute results.

Enhancing the performance or optimizing the tool for larger networks.

License:
This project is licensed under the MIT License. See the LICENSE file for more details.

This description provides a comprehensive overview of the tool's functionality, how it works, and how others can use and contribute to it. It is more detailed and covers the features and technical details thoroughly. Feel free to replace any placeholders (like your username or repository URL) with actual details.
