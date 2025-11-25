# Hidden in Plain Sight

**Category:** Forensics
**Author:** Pulgaa
**Points:** 500

## 📝 Description

A SOC analyst captured network traffic from a suspected compromised workstation. Intelligence suggests the malware uses a covert channel to exfiltrate data character-by-character, hiding among normal network traffic. Your job is to analyze the packet capture and uncover what the attackers stole.

## 📁 Provided Files

- `challenge.pcapng` – Network packet capture containing mixed traffic (TCP, UDP, ICMP, ARP, DNS, and malicious C2 communication)

## 🎯 Goal

Analyze the network traffic, identify the malicious communication channel, and extract the exfiltrated flag.

---

**Flag Format:** `Securinets_fst{h1dd3n_1n_pl41n_s1ght}`
