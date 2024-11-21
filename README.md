# Nmap Scanner Tool

## Overview
This Python tool automates network scanning using **Nmap**. It reads a list of IP addresses from a text file, scans each IP, and saves the results in an Excel file. The scan results are also displayed in the console.

---

## Features
- Reads a list of IPs from a text file (`ips.txt`).
- Executes an Nmap scan with options: `-sT -p- -Pn`.
- Displays the scan results in the console.
- Exports the results to an Excel file (`nmap_results.xlsx`).

---

## Requirements

### Prerequisites
1. Python 3.6 or higher.
2. Python packages:
   - `pandas`
   - `openpyxl` (for Excel file generation).
3. **Nmap** installed and available in the system's PATH.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nmap-scanner-tool.git
   cd nmap-scanner-tool
