import sys
import time
import cmd
import os
import subprocess
import platform
import socket
from tqdm import tqdm

print("╔╗╔═╗░░░░░░░░░╔╗░░░░░░░░")
print("║║║╔╝░░░░░░░░░║║░░░░░░░░")
print("║╚╝╝╔╗╔╦╗╔╦══╣╚═╦╦═╦══╗")
print("║╔╗║║║║║╚╝║╔╗║╔╗╠╣╔╣╔╗║")
print("║║║╚╣╚╝║║║║╚╝║║║║║║║╔╗║")
print("╚╝╚═╩══╩╩╩╩══╩╝╚╩╩╝╚╝╚╝")
print("Developed by Jose")
print("")
print("Preparing...")
print("")

time.sleep(5)

def progress_bar(current, total, bar_length=50):
    progress = float(current) / total
    arrow = '-' * int(progress * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write(f'\r{current}/{total} [{arrow}{spaces}] {int(progress * 99)}%')
    sys.stdout.flush()

def countdown(total_time, interval):
    start_time = time.time()
    remaining_time = total_time

    while remaining_time > 0:
        time.sleep(interval)
        remaining_time = total_time - (time.time() - start_time)
        progress_bar(total_time - remaining_time, total_time)

    print()
    print("")
    print("Complete!")

total_time = 2 # Total time for the progress bar to complete in seconds
interval = 0.1 # Interval at which the progress bar is updated in seconds

countdown(total_time, interval)

print("")

def get_os_info():
    """Retrieves basic operating system information."""
    os_name = platform.system()
    os_release = platform.release()
    return f"Operating System: {os_name} {os_release}"

def get_processor_info():
    """Retrieves processor information."""
    if platform.system() in ("Windows", "Linux", "Darwin"):  # Check for supported OSes
        if platform.system() == "Windows":
            try:
                import wmi
                c = wmi.WMI()
                processor = c.Win32_Processor()[0]
                return f"Processor: {processor.Name} ({processor.NumberOfCores} cores)"
            except ImportError:
                output = subprocess.check_output("wmic cpu get name", shell=True, encoding="utf-8")
                return f"Processor: {output.strip()}"
        else:
            return f"Processor: {platform.processor()}"
    else:
        return "Unable to identify processor information."

def get_ram_info():
    """Retrieves RAM information."""
    if platform.system() in ("Windows", "Linux", "Darwin"):
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic memorychip get capacity", shell=True, encoding="utf-8")
            total_memory_mb = sum(int(line.split()[1]) for line in output.splitlines()[1:])
            return f"RAM: {total_memory_mb / 1024} GB"
        else:
            import psutil
            virtual_memory = psutil.virtual_memory()
            return f"RAM: {virtual_memory.total / (1024 * 1024 * 1024):.2f} GB"
    else:
        return "Unable to identify RAM information."

def get_address_info():
    """Retrieves IP address information."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return f"Address: {hostname} ({ip_address})"
    except socket.error as e:
        return "Unable to identify address information."

# Print the gathered information
print(get_os_info())
print(get_processor_info())
print(get_ram_info())
print(get_address_info())

time.sleep(2)
print("")

def run_command(command):
    """Executes the given command and returns its output."""
    result = os.popen(command).read()
    return result

def handle_kumohira_optimize():
    print("Optimizing...")
    # Create and manage the progress bar within this function
    pbar = tqdm(total=100)
    for i in range(100):
        time.sleep(0.03)
        pbar.update(1)
    pbar.close()

    # Replace with any optimization logic you need

while True:
    prompt = input(">>> ")

    if prompt.startswith("Kumohira --optimize"):
        handle_kumohira_optimize()  # Call the function only when the command is entered
    else:
        output = run_command(prompt)
        print(output)