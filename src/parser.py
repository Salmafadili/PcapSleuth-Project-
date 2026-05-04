import pandas as pd
from scapy.all import rdpcap, IP, TCP, UDP, DHCP
import matplotlib.pyplot as plt

def extract_to_dataframe(pcap_file):
    try:
        packets = rdpcap(pcap_file)
        data = []
        for pkt in packets:
            if IP in pkt:
                packet_info = {
                    "src": pkt[IP].src,
                    "src_mac": pkt.src,
                    "dst": pkt[IP].dst,
                    "proto": pkt[IP].proto,
                    "size": len(pkt),
                    "sport": pkt.sport if (TCP in pkt or UDP in pkt) else None,
                    "dport": pkt.dport if (TCP in pkt or UDP in pkt) else None,
                    "hostname": None
                }
                if pkt.haslayer(DHCP):
                    options = pkt['DHCP'].options
                    for opt in options:
                        if isinstance(opt, tuple) and opt[0] == 'hostname':
                            packet_info["hostname"] = opt[1].decode(errors='ignore')
                data.append(packet_info)
        return pd.DataFrame(data)
    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def detect_port_scan(df, threshold=20):
    print("\n[!] Scanning for Port Scan activities...")
    scanner_results = df.groupby('src')['dport'].nunique()
    suspicious_ips = scanner_results[scanner_results > threshold]
    if not suspicious_ips.empty:
        for ip, count in suspicious_ips.items():
            print(f"⚠️  ALERT: {ip} scanned {count} unique ports!")
    else:
        print("✅ No suspicious port scanning detected.")

def plot_top_ips(df):
    plt.figure(figsize=(10, 6))
    df['src'].value_counts().head(5).plot(kind='bar', color='skyblue')
    plt.title('Top 5 Source IPs by Packet Count')
    plt.xlabel('IP Address')
    plt.ylabel('Number of Packets')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data/traffic_chart.png')
    print("\n[+] Chart saved as data/traffic_chart.png")
    plt.show()

if __name__ == "__main__":
    pcap_path = "data/2025-01-22-traffic-analysis-exercise.pcap" 
    df = extract_to_dataframe(pcap_path)
    
    if df is not None and not df.empty:
        print(f"\n[*] Analysis Complete. Packets: {len(df)}")
        print(df[['src', 'src_mac', 'dst', 'proto', 'hostname']].head(10))
        detect_port_scan(df)
        plot_top_ips(df)
        df.to_csv("data/analysis_results.csv", index=False)
        print("[+] Results exported to data/analysis_results.csv")
    else:
        print("[!] No data found. Check file path and unzip if necessary.")
