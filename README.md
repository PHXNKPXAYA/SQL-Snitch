
# SQL Snitch - SQL Injection Scanner

**SQL Snitch** is a tool designed to scan web applications for SQL injection vulnerabilities. It automates the process of testing different SQL injection payloads against a target website and checks for vulnerabilities based on common SQL errors in the response. This tool is for **educational purposes only** and should only be used with permission.

---

## Features

- **SQL Injection Scanning**: Automatically scans websites for SQL injection vulnerabilities using predefined payloads.
- **Multiple Scan Types**: Choose between different scan depths:
  - **Light**: Basic injection payloads.
  - **Deep**: More complex payloads for a deeper scan.
  - **Full**: A comprehensive scan using a wider range of payloads.
- **Parameter Scanning**: Scan specific URL parameters for SQL injection vulnerabilities.
- **Progress Tracking**: Uses `tqdm` to provide a real-time progress bar, displaying estimated time for the scan completion.
- **Error Detection**: Detects common SQL error messages to identify potential vulnerabilities.
- **Command-Line Interface**: Simple command-line interface for easy interaction and input.

---

## Installation

To use **SQL Snitch**, ensure that you have Python 3.x installed on your system.

### Required Libraries

You must install the following libraries:

```bash
pip install requests tqdm
```

---

## Usage

1. **Run the Script**: Launch the script in your terminal.

```bash
python sql_snitch.py
```

2. **Enter URL**: You will be prompted to enter the base URL you want to scan.

3. **Choose Scan Type**: Select a scan type (`light`, `deep`, or `full`).

4. **Provide Parameters** (optional): If the URL contains parameters, input them in `key=value` format (comma-separated).

5. **Scan Progress**: The script will display a progress bar and show any found vulnerabilities.

---

## Example

```bash
Enter the base URL to scan: https://example.com/product.php?id=1
Choose scan type (light, deep, full): deep
Enter parameters in key=value format (comma-separated) or leave blank: id=1
```

---

## License

This project is licensed under the MIT License. See the **[LICENSE](LICENSE)** file for more details.

---

## Acknowledgments

- **TQDM**: Used for progress bar functionality.
- **Requests**: Used to handle HTTP requests and responses.

---

## Disclaimer

This tool is intended for **educational purposes only**. **SQL Snitch** should only be used to test websites and applications you have explicit permission to scan. Misuse of this tool is not encouraged, and the author is not responsible for any illegal activities or damages.

---

## 💙 Support My Work

If you find **SQL Snitch** useful and want to support my work, feel free to buy me a coffee! Your support helps fund future development and improvements.

[Support me on Buy Me a Coffee](https://buymeacoffee.com/phxnkpxaya)

Thank you for your generosity! ☕️
