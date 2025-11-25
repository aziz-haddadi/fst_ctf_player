from Crypto.Cipher import AES
import base64

key = base64.b64decode("h828g15uDWihrcUWAATMEqHibYXSBERjPWEKFPSbQtc=")
iv = key[:16]

print(f"Key: {key.hex()}")
print(f"IV: {iv.hex()}\n")

with open('dns.txt', 'r') as f:
    lines = f.readlines()

hex_values = []
for i in range(0, len(lines), 4):
    line = lines[i].strip()
    if line:
        hex_part = line.split('.txt')[0]
        hex_values.append(hex_part)

print(f"Processing {len(hex_values)} hex values (every 4th line)\n")
print("=" * 60)

decrypted_parts = []
for hex_val in hex_values:
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct = bytes.fromhex(hex_val)
        pt = cipher.decrypt(ct)
        
        unpadded = pt[:-pt[-1]]
        
        decoded = unpadded.decode('utf-8', errors='ignore')
        decrypted_parts.append(decoded)
        print(f"Hex: {hex_val}")
        print(f"Decrypted: {decoded}")
        print("-" * 60)
    except Exception as e:
        print(f"Hex: {hex_val}")
        print(f"Error: {e}")
        print("-" * 60)

final_flag = ''.join(decrypted_parts)

print("FINAL FLAG:")
print(final_flag)
