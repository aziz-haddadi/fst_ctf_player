#!/usr/bin/env python3
from scapy.all import *

# Load the packet capture
packets = rdpcap("challenge.pcapng")

# Filter for TCP packets to port 4444 with payload data
flag_chars = []

for pkt in packets:
    # Check if packet has TCP and Raw (data) layers
    if TCP in pkt and Raw in pkt:
        # Check if destination port is 4444
        if pkt[TCP].dport == 4444:
            # Get the payload
            payload = bytes(pkt[Raw].load)
            
            # Extract the first byte
            if len(payload) > 0:
                first_char = chr(payload[0])
                flag_chars.append(first_char)
                print(f"Found character: {first_char}")

# Assemble the flag
flag = ''.join(flag_chars)
print(f"\n🚩 Flag: {flag}")
