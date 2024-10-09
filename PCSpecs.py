import platform
import psutil
import GPUtil
import subprocess
import re
from colorama import Fore, Style, init
import speedtest

# Initialize colorama
init(autoreset=True)

def get_system_info():
    """Get basic system info."""
    os_info = platform.system() + " " + platform.release()
    cpu_info = platform.processor()
    ram_info = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    motherboard_info = get_motherboard_info()
    gpu_info = get_gpu_info()
    return os_info, cpu_info, ram_info, motherboard_info, gpu_info

def get_motherboard_info():
    """Attempt to get motherboard information (works on Windows and Linux)."""
    if platform.system() == "Windows":
        try:
            output = subprocess.check_output("wmic baseboard get product,Manufacturer", shell=True).decode()
            return output.split("\n")[1].strip()
        except Exception:
            return "Unknown"
    elif platform.system() == "Linux":
        try:
            with open('/sys/devices/virtual/dmi/id/board_vendor') as f:
                vendor = f.read().strip()
            with open('/sys/devices/virtual/dmi/id/board_name') as f:
                name = f.read().strip()
            return f"{vendor} {name}"
        except Exception:
            return "Unknown"
    return "Unknown"

def get_gpu_info():
    """Get GPU information."""
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        return f"{gpu.name} (Driver Version: {gpu.driver})"
    return "No GPU found"

def get_internet_speeds():
    """Get internet ping, upload, and download speeds."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        ping = st.results.ping
        download_speed = st.download() / (1024 ** 2)  # Convert to Mbps
        upload_speed = st.upload() / (1024 ** 2)      # Convert to Mbps
        return ping, upload_speed, download_speed
    except Exception:
        return None, None, None

def compare_specs_with_game(cpu, ram, gpu, game_name, game_specs):
    """Compare the system specs with game requirements."""
    cpu_met = cpu.lower() in game_specs['cpu'].lower()
    ram_met = ram >= game_specs['ram']
    gpu_met = gpu.lower() in game_specs['gpu'].lower()
    
    if cpu_met and ram_met and gpu_met:
        status = f"{Fore.GREEN}Exceeds Optimized Requirements"
    elif cpu_met and ram_met:
        status = f"{Fore.YELLOW}Meets Recommended Requirements"
    elif cpu_met or ram_met or gpu_met:
        status = f"{Fore.YELLOW}Meets Minimum Requirements"
    else:
        status = f"{Fore.RED}Does NOT Meet Requirements"
    return status

def print_specs():
    """Print system specs."""
    os_info, cpu_info, ram_info, motherboard_info, gpu_info = get_system_info()
    print(f"{Fore.BLUE}System Intel Pro")
    print(f"{Fore.BLUE}Developed by: Dr. Aubrey W. Love II (AKA Rogue Payload)")
    print(f"{Fore.BLUE}A product of Global Bug Hunters\n")
    print(f"{Fore.CYAN}Hardware Specs:")
    print(f"{Fore.CYAN}CPU: {cpu_info}")
    print(f"{Fore.CYAN}RAM: {ram_info:.2f} GB")
    print(f"{Fore.CYAN}GPU: {gpu_info}")
    print(f"{Fore.CYAN}Motherboard: {motherboard_info}\n")

    print(f"{Fore.CYAN}Internet Specs:")
    ping, upload_speed, download_speed = get_internet_speeds()
    if ping is not None:
        print(f"{Fore.CYAN}Ping Rate: {ping} ms")
        print(f"{Fore.CYAN}Upload Speeds: {upload_speed:.2f} Mbps")
        print(f"{Fore.CYAN}Download Speeds: {download_speed:.2f} Mbps")
    else:
        print(f"{Fore.RED}Could not retrieve internet speed information.\n")

    # Game specs for comparison
    game_requirements = {
        "Call of Duty": {
            "cpu": "i3-4340",
            "ram": 8,
            "gpu": "GTX 670"
        },
        "Fortnite": {
            "cpu": "i5-7300U",
            "ram": 16,
            "gpu": "GTX 960"
        },
        "Roblox": {
            "cpu": "i3-3225",
            "ram": 8,
            "gpu": "HD 4000"
        },
        "Minecraft": {
            "cpu": "i3-4150",
            "ram": 8,
            "gpu": "HD 4400"
        }
    }

    print(f"{Fore.BLUE}\nGame Compatibility Check:")
    for game_name, specs in game_requirements.items():
        status = compare_specs_with_game(cpu_info, ram_info, gpu_info, game_name, specs)
        print(f"{Fore.MAGENTA}{game_name}: {status}")

if __name__ == "__main__":
    print_specs()
