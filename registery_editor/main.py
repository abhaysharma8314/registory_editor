import subprocess

def block_usb_ports():
    try:
        # Disable USB Ports using PowerShell
        usb_script = """
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR" -Name "Start" -Value 4
        """
        subprocess.run(["powershell", "-Command", usb_script], check=True)
        print("USB ports are blocked.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to block USB ports: {e}")

def disable_bluetooth():
    try:
        # Disable Bluetooth using PowerShell
        bluetooth_script = """
        Disable-WindowsOptionalFeature -Online -FeatureName "Bluetooth"
        """
        subprocess.run(["powershell", "-Command", bluetooth_script], check=True)
        print("Bluetooth is disabled.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to disable Bluetooth: {e}")

def restrict_command_prompt():
    try:
        # Restrict Command Prompt using PowerShell
        cmd_prompt_script = """
        Set-ItemProperty -Path "HKCU:\\Software\\Policies\\Microsoft\\Windows\\System" -Name "DisableCMD" -Value 1
        """
        subprocess.run(["powershell", "-Command", cmd_prompt_script], check=True)
        print("Command Prompt is restricted.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restrict Command Prompt: {e}")

def block_website(website):
    try:
        # Modify the hosts file to block the website
        hosts_entry = f"127.0.0.1 {website}\n"
        with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as hosts_file:
            hosts_file.write(hosts_entry)
        print(f"Access to {website} is blocked.")
    except Exception as e:
        print(f"Failed to block {website}: {e}")

if __name__ == "__main__":
    # Run the security measures
    block_usb_ports()
    disable_bluetooth()
    restrict_command_prompt()

    # Block access to facebook.com
    block_website("facebook.com")