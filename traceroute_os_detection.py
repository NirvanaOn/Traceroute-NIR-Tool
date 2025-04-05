from scapy.all import IP, ICMP, sr1
import time
import socket
import ipaddress
import requests

log = True

def logmessage(message):
    if log:
        with open("Traceroute_logs.txt",'a') as log_file:
            log_file.write(f"{message}\n")

def getlocation(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        data = response.json()
        if data["status"] == "success":
            return {
                "country": data["country"],
                "city": data["city"],
                "lat": data["lat"],
                "lon": data["lon"]
            }
        else:
            return {"country": "Unknown", "city": "Unknown", "lat": 0, "lon": 0}
    except:
        return {"country": "Error", "city": "Error", "lat": 0, "lon": 0}


def detect_rtt_spike(current_rtt, previous_rtt):
    return previous_rtt is not None and current_rtt > previous_rtt * 3


def is_private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False


def is_ttl_suspicious(reply_ttl, sent_ttl):
    return reply_ttl <= 1 < sent_ttl


def sendicmpwithttl(tar_ip, max_hops=30):
    print(f"Tracing route to {tar_ip}...\n")
    prev_rtt = None
    try:
        resolve_ip = socket.gethostbyname(tar_ip)
    except socket.gaierror:
        print("Invalid domain or IP.")
        return

    for ttl in range(1, max_hops + 1):
        iplayer = IP(dst=tar_ip, ttl=ttl)
        icmplayer = ICMP()
        packet = iplayer / icmplayer
        start_time = time.time()
        reply = sr1(packet, timeout=2, verbose=0)
        end_time = time.time()

        if reply:
            rtt = round((end_time - start_time) * 1000, 2)
            spoof_flags = []

            if is_ttl_suspicious(reply.ttl, ttl):
                spoof_flags.append("Suspicious TTL")

            if is_private_ip(reply.src) and not is_private_ip(resolve_ip):
                spoof_flags.append("Private IP in public trace")

            if detect_rtt_spike(rtt, prev_rtt):
                spoof_flags.append("RTT Spike")

            prev_rtt = rtt
            location = getlocation(reply.src)

            flag_text = f"{' | '.join(spoof_flags)}" if spoof_flags else "TTL Normal"
            message = f"Hop {ttl} : {reply.src} || RTT : {rtt}ms || TTL = {reply.ttl} || OS Detected : {guess_os(reply.ttl)} || Location Found : ({location['country']},{location['city']},{location['lat']},{location['lon']}) || {flag_text}"
            print(message)
            logmessage(message)

            if reply.src == resolve_ip:
                print("Destination Reached")
                ostype = guess_os(reply.ttl)
                print(f"OS of Destination : {ostype}")
                break
        else:
            print(f"Hop {ttl} : No Reply")


def guess_os(ttl):
    if ttl <= 64:
        return "Linux/Unix"
    elif ttl <= 128:
        return "Windows"
    elif ttl <= 255:
        return "Cisco/Networking Device"
    else:
        return "Unknown"


try:
    target = input("Enter IP or Domain : ").strip()
    sendicmpwithttl(target)
except socket.gaierror:
    print("Invalid domain name.")
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
