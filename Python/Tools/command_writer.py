import subprocess
import os

file_name = "server_security_report.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write("=== SERVER SECURITY REPORT ===\n")
    
    p1 = subprocess.run(['systemctl', 'list-units', '--type=service', '--state=running'], stdout=f, text=True)

if p1.returncode != 0:
    print("[-] Error executing the command")
else:
    print(f"[+] Done! Report saved to: {os.path.join(os.getcwd(), file_name)}")