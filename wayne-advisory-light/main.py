#!/usr/bin/env python3
"""
Task 3: Your Own Idea - Basic CLI Application Template

This is a starting template for your AI-assisted application project.
Replace this with your own idea and implementation.
"""
from datetime import datetime
import json
import os
import socket


class WayneAdvisory:

    def __init__(self, authorized_assets_file="wayne_secure_baseline.json"):
        self.authorized_assets_file = authorized_assets_file
        self.authorized_macs = self.load_secure_baseline()

    def detect_network_perimeter(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return ".".join(local_ip.split(".")[:-1]) + ".0/24"
        except Exception:
            return "192.168.1.0/24"

    def load_secure_baseline(self):
        if os.path.exists(self.authorized_assets_file):
            try:
                with open(self.authorized_assets_file, "r") as f:
                    return set(json.load(f))
            except Exception:
                print("[!] Error reading baseline. Initialized as empty.")
                return set()
        return set()

    def save_secure_baseline(self, mac_list):
        with open(self.authorized_assets_file, "w") as f:
            json.dump(list(mac_list), f, indent=4)
        self.authorized_macs = set(mac_list)
        print(f"\n[+] Baseline successfully updated with {len(mac_list)} assets.")

    def run_perimeter_discovery(self, ip_range):
        print(f"\n[*] Sweeping perimeter coordinates: {ip_range}...")
        base_net = ".".join(ip_range.split(".")[:-1])

        simulated_hosts = [f"{base_net}.1", f"{base_net}.15", f"{base_net}.102"]
        return simulated_hosts

    def execute_component_audit(self, target_ip):
      
        critical_ports = [80, 443, 8080]
        vulnerabilities = []

        for port in critical_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            s.close()

            if result == 0: 
                risk = "Medium - Interface Exposed"
                if port == 80:
                    risk = "HIGH - Unencrypted Administration Interface Open"

                vulnerabilities.append({
                    "port": port,
                    "service": "http" if port in [80, 8080] else "https",
                    "risk_assessment": risk
                })

        return vulnerabilities

    def generate_executive_brief(self, ip_range):
        hosts = self.run_perimeter_discovery(ip_range)

        print("\n" + "=" * 85)
        print("                      WAYNE ADVISORY PRIVACY REPORT                          ")
        print("=" * 85)
        print(f"Analysis Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Perimeter Size: {len(hosts)} active simulated devices detected.")
        print("-" * 85)
        print(f"{'IP Address':<15} {'MAC Address':<19} {'Security Integrity'}")
        print("-" * 85)

        mock_macs = ["00:1A:2B:3C:4D:5E", "00:1A:2B:3C:4D:6F", "UNKNOWN"]
        anomalous_targets = []

        for i, host in enumerate(hosts):
            mac = mock_macs[i % len(mock_macs)]

            if len(self.authorized_macs) > 0 and mac not in self.authorized_macs and mac != "UNKNOWN":
                status = "ANOMALOUS / UNKNOWN"
            elif mac == "UNKNOWN":
                status = "Unverified Component"
            else:
                status = "Verified Baseline"

            print(f"{host:<15} {mac:<19} {status}")

            if status in ["ANOMALOUS / UNKNOWN", "Unverified Component"]:
                anomalous_targets.append(host)

        if anomalous_targets:
            print("\n" + "-" * 85)
            print("DEEP COMPONENT EXPOSURE LOGS (Simulated socket sweep)")
            print("-" * 85)
            for target_ip in anomalous_targets:
                exposures = self.execute_component_audit(target_ip)
                if exposures:
                    print(f"\n[!] Vulnerability on Node: {target_ip}")
                    for exp in exposures:
                        print(f"    -> Port {exp['port']}/{exp['service']}")
                        print(f"       Risk Severity: {exp['risk_assessment']}")
                else:
                    print(f"\n[+] Node Verified: {target_ip} - Offline or Fully Firewalled.")

        print("\n" + "=" * 85)


def operational_terminal():
    engine = WayneAdvisory()

    print("=" * 60)
    print("         WAYNE ADVISORY - PRIVATE OPERATIONAL TERMINAL       ")
    print("=" * 60)
    print("[+] Light-weight environment configuration active.")

    default_subnet = engine.detect_network_perimeter()
    target_network = input(f"\nEnter network perimeter [{default_subnet}]: ").strip()
    if not target_network:
        target_network = default_subnet

    while True:
        print("\n--- WAYNE ADVISORY OPERATIONS DIRECTIVE ---")
        print("1) Generate Executive Estate Privacy Report")
        print("2) Snapshot & Lock Verified Secure Baseline")
        print("3) Run Local Component Audit on Target IP")
        print("4) Review Local Security Baseline Database")
        print("5) Securely Terminate Session")

        choice = input("\nSelect operational directive (1-5): ").strip()

        if choice == "1":
            engine.generate_executive_brief(target_network)

        elif choice == "2":
            print(f"\n[*] Generating active signature maps on {target_network}...")
            # Automatically baseline our safe mocked signatures
            mock_macs = ["00:1A:2B:3C:4D:5E", "00:1A:2B:3C:4D:6F"]
            confirm = input("Lock mock signatures into baseline file? (y/n): ").strip().lower()
            if confirm == "y":
                engine.save_secure_baseline(mock_macs)
            else:
                print("[*] Operation aborted.")

        elif choice == "3":
            target_ip = input("\nEnter target IP (e.g., 127.0.0.1 or 192.168.1.1): ").strip()
            if target_ip:
                print(f"[*] Auditing connection responses on: {target_ip}")
                vulns = engine.execute_component_audit(target_ip)
                if vulns:
                    print(f"\n[!!!] SUB-SYSTEM EXPOSURES DETECTED FOR {target_ip}:")
                    print(json.dumps(vulns, indent=4))
                else:
                    print(f"\n[+] Node Clean: No common management ports open on {target_ip}.")
            else:
                print("[!] Error: Target IP cannot be empty.")

        elif choice == "4":
            print(f"\n[i] Security Matrix: {len(engine.authorized_macs)} signatures verified.")
            if engine.authorized_macs:
                print(f"Verified Signatures: {list(engine.authorized_macs)}")

        elif choice == "5":
            print("\n[-] Session safely terminated.")
            break
        else:
            print("[!] Invalid directive. Try again.")


if __name__ == "__main__":
    operational_terminal()
