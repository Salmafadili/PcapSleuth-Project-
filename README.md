# 🛡️ PcapSleuth: Network Traffic Anomaly Detection Tool

**PcapSleuth** is a Digital Forensics and Incident Response (DFIR) tool developed as part of a technical internship project. It automates the triage and analysis of network traffic, transforming raw PCAP data into actionable security intelligence to identify threats that are often missed during manual inspection.

---

## 🌟 Key Value Proposition
In modern security environments, manual analysis of thousands of packets is inefficient. **PcapSleuth** bridges this gap by:
*   **Automating Metadata Extraction**: Instant identification of Source/Destination IPs, MAC addresses, and protocols.
*   **Behavioral Threat Detection**: Algorithmic detection of reconnaissance activities like **Port Scanning**.
*   **Contextual Awareness**: Extracting hostnames from DHCP traffic to identify devices within the internal network.

## 🚀 Technical Features
*   **Deep Packet Inspection (DPI)**: Utilizes `Scapy` to parse complex network layers (IP, TCP, UDP, DHCP).
*   **Security Heuristics**: Implements threshold-based detection to alert on suspicious scanning behavior (e.g., a single IP scanning multiple unique ports).
*   **Data Science Integration**: Uses `Pandas` for high-speed packet processing and structured data export (CSV).
*   **Visual Intelligence**: Generates automated traffic distributions using `Matplotlib` to highlight anomalies visually.

## 📂 Project Architecture
```text
PCAPSLEUTH/
│
├── data/                             # Data directory for network captures and outputs
│   ├── 2025-01-22-traffic-analysis... # Real malware PCAP file used for baseline validation
│   ├── analysis_results.csv          # Generated analysis results report in CSV format
│   ├── exercise.pcap.zip             # Compressed archive containing the capture file
│   └── traffic_chart.png             # Generated visualization chart of network traffic
│
├── src/                              # Source code directory
│   └── parser.py                     # Main Python script for parsing and intrusion detection
│
├── venv/                             # Python Virtual Environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── share/
│
├── .gitignore                        # Git exclusion file (e.g., ignoring large PCAP files)
├── README.md                         # Project documentation (This file)
└── requirements.txt                  # List of required external libraries (Scapy, Pandas, etc.)


