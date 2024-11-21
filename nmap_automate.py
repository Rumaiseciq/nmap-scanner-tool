import os
import subprocess
import pandas as pd

def run_nmap(ip):
    """
    Runs the nmap command for a given IP and returns the output as a string.
    """
    try:
        command = ["nmap", "-sT", "-p-", "-Pn", ip]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error scanning {ip}: {e}"

def process_ip_list(input_file, output_excel):
    """
    Reads the list of IPs from a text file, runs nmap on each, displays results in the console, 
    and saves results in an Excel file.
    """
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist.")
        return

    # Read IPs from the input file
    with open(input_file, "r") as file:
        ips = [line.strip() for line in file if line.strip()]
    
    if not ips:
        print("No IPs found in the input file.")
        return

    # Prepare data for the Excel file
    data = []
    for ip in ips:
        print(f"Scanning IP: {ip}")
        result = run_nmap(ip)
        print(f"Scan result for {ip}:\n{result}\n")  # Ensure the result is displayed here
        data.append({"IP": ip, "Result": result})

    # Save results to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False)
    print(f"Results saved to {output_excel}")

if __name__ == "__main__":
    input_file = "ips.txt"  # Input file containing the list of IPs
    output_excel = "nmap_results.xlsx"  # Output Excel file
    process_ip_list(input_file, output_excel)
