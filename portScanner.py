import socket
from datetime import datetime


COMMON_PORTS = {
    20: "FTP (Data Transfer)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Proxy",
}

def port_scanner():
    print("Welcome to the Python Port Scanner with Logging!")
    
  
    target = input("Enter the domain or IP address to scan: ").strip()
    
   
    try:
        target_ip = socket.gethostbyname(target)
        print(f"\nScanning target: {target} ({target_ip})")
    except socket.gaierror:
        print("Error: Unable to resolve domain.")
        return

  
    log_filename = f"port_scan_log_{target}.txt"
    with open(log_filename, "w") as log_file:
       
        log_file.write(f"Port Scan Results for {target} ({target_ip})\n")
        log_file.write(f"Scan started: {datetime.now()}\n")
        log_file.write(f"{'Port':<10}{'Status':<10}{'Service':<30}\n")
        log_file.write("=" * 50 + "\n")

        print("Scanning all 65535 ports... This might take some time.")

        
        start_time = datetime.now()

      
        for port in range(1, 65536):
            try:
               
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)  
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    service = COMMON_PORTS.get(port, "Unknown Service")
                    result_line = f"{port:<10}Open      {service:<30}\n"
                    print(result_line.strip())
                    log_file.write(result_line)
                s.close()
            except KeyboardInterrupt:
                print("\nExiting program.")
                break
            except Exception as e:
                print(f"Error scanning port {port}: {e}")

       
        end_time = datetime.now()
        total_time = end_time - start_time

        log_file.write("=" * 50 + "\n")
        log_file.write(f"Scan completed: {datetime.now()}\n")
        log_file.write(f"Total scan duration: {total_time}\n")

    print(f"\nScanning completed in {total_time}.")
    print(f"Results saved to {log_filename}")

if __name__ == "__main__":
    port_scanner()
