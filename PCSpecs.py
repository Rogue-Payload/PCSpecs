import platform
import psutil
import GPUtil
import subprocess
from colorama import Fore, Style, init
import speedtest

# Initialize colorama for colored terminal output
init(autoreset=True)

def log_message(message, log_type="info"):
    """Log message with different colors based on log type."""
    colors = {
        "info": Fore.CYAN,
        "success": Fore.GREEN,
        "warning": Fore.YELLOW,
        "error": Fore.RED
    }
    color = colors.get(log_type, Fore.CYAN)
    print(f"{color}{message}{Style.RESET_ALL}")

def get_system_info():
    """Retrieve system specifications."""
    os_info = f"{platform.system()} {platform.release()}"
    cpu_info = get_cpu_info()
    ram_info = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
    motherboard_info = get_motherboard_info()
    gpu_info = get_gpu_info()
    return os_info, cpu_info, ram_info, motherboard_info, gpu_info

def get_motherboard_info():
    """Get motherboard information based on the operating system."""
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic baseboard get product,Manufacturer", shell=True).decode()
            return output.split("\n")[1].strip()
        elif platform.system() == "Linux":
            with open('/sys/devices/virtual/dmi/id/board_vendor') as vendor_file:
                vendor = vendor_file.read().strip()
            with open('/sys/devices/virtual/dmi/id/board_name') as name_file:
                name = name_file.read().strip()
            return f"{vendor} {name}"
        elif platform.system() == "Darwin":  # macOS
            output = subprocess.check_output("system_profiler SPHardwareDataType", shell=True).decode()
            for line in output.splitlines():
                if "Model Name" in line:
                    return line.split(": ")[1]
    except Exception as e:
        log_message(f"[ERROR] Failed to get motherboard info: {str(e)}", log_type="error")
        return "Unknown"


def get_cpu_info():
    """Get detailed CPU information."""
    try:
        if platform.system() == "Linux":
            command = "lscpu | grep 'Model name'"
            result = subprocess.check_output(command, shell=True).decode()
            cpu_name = result.split(":")[1].strip() if ':' in result else "Unknown CPU"
        elif platform.system() == "Darwin":  # macOS
            cpu_name = subprocess.check_output("sysctl -n machdep.cpu.brand_string", shell=True).decode().strip()
        else:
            cpu_name = platform.processor()

        cpu_cores = psutil.cpu_count(logical=True)
        physical_cores = psutil.cpu_count(logical=False)
        cpu_freq = psutil.cpu_freq().current
        return f"{cpu_name} ({physical_cores} physical cores, {cpu_cores} logical cores) at {cpu_freq:.2f} MHz"
    except Exception as e:
        log_message(f"[ERROR] Could not retrieve CPU information: {e}", log_type="error")
        return "Unknown CPU"


def get_gpu_info():
    """Get GPU information using platform-specific methods."""
    try:
        if platform.system() == "Windows" or platform.system() == "Linux":
            # Use GPUtil for Windows/Linux
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                log_message(f"Detected GPU: {gpu.name} (Driver Version: {gpu.driver})", log_type="info")
                return f"{gpu.name} (Driver Version: {gpu.driver})"
            # Fallback to lshw if GPUtil fails (Linux only)
            if platform.system() == "Linux":
                output = subprocess.check_output("lshw -C display", shell=True).decode('utf-8')
                for line in output.splitlines():
                    if 'product:' in line:
                        gpu_name = line.strip().split(": ")[1]
                        log_message(f"Detected GPU using lshw: {gpu_name}", log_type="info")
                        return gpu_name
        elif platform.system() == "Darwin":  # macOS
            output = subprocess.check_output("system_profiler SPDisplaysDataType", shell=True).decode()
            for line in output.splitlines():
                if "Chipset Model" in line:
                    gpu_name = line.split(": ")[1].strip()
                    log_message(f"Detected GPU using system_profiler: {gpu_name}", log_type="info")
                    return gpu_name
        return "No GPU found"
    except Exception as e:
        log_message(f"[ERROR] Failed to detect GPU: {e}", log_type="error")
        return "Unknown GPU"



def test_internet_speed():
    """Check internet speed using Speedtest."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 10**6  # Convert to Mbps
        upload_speed = st.upload() / 10**6  # Convert to Mbps
        ping = st.results.ping
        log_message(f"[INFO] Internet speed - Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping:.2f} ms")
        return download_speed, upload_speed, ping
    except Exception as e:
        log_message(f"[ERROR] Failed to test internet speed: {str(e)}", log_type="error")
        return None, None, None

def compare_specs_with_game(cpu, ram, gpu, game_name, game_specs):
    """Compare the system specs with game requirements."""
    cpu_met = any(spec.lower() in cpu.lower() for spec in game_specs['cpu'])
    ram_met = ram >= game_specs['ram']
    gpu_met = any(spec.lower() in gpu.lower() for spec in game_specs['gpu'])
    
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
    """Print system specs and compare them with popular game requirements."""
    os_info, cpu_info, ram_info, motherboard_info, gpu_info = get_system_info()
    log_message(f"System Intel Pro", log_type="info")
    log_message(f"Developed by: Dr. Aubrey W. Love II (AKA Rogue Payload)", log_type="info")
    log_message(f"A product of Global Bug Hunters\n", log_type="info")

    log_message(f"Hardware Specs:", log_type="info")
    log_message(f"CPU: {cpu_info}")
    log_message(f"RAM: {ram_info:.2f} GB")
    log_message(f"GPU: {gpu_info}")
    log_message(f"Motherboard: {motherboard_info}\n")

    download_speed, upload_speed, ping = test_internet_speed()
    log_message(f"Internet Specs:", log_type="info")
    if download_speed:
        log_message(f"Ping: {ping:.2f} ms, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")
    else:
        log_message("Could not retrieve internet speed information.", log_type="error")

    # Define game specs for comparison
    game_requirements = {
        "Call of Duty": {
            "cpu": ["i3-4340", "FX-6300"],
            "ram": 8,
            "gpu": ["GTX 670", "GTX 1650"]
        },
        "Fortnite": {
            "cpu": ["i5-7300U", "R3 3300U"],
            "ram": 16,
            "gpu": ["GTX 960", "R9 280"]
        },
        "Roblox": {
            "cpu": ["1.6 GHz", "Dual-core"],
            "ram": 4,
            "gpu": ["DX10", "Dedicated GPU"]
        },
        "Minecraft": {
            "cpu": ["i3-4150", "N4100"],
            "ram": 8,
            "gpu": ["HD 4400", "R5 series"]
        }
    }

    log_message("\nGame Compatibility Check:", log_type="info")
    for game_name, specs in game_requirements.items():
        status = compare_specs_with_game(cpu_info, ram_info, gpu_info, game_name, specs)
        log_message(f"{game_name}: {status}")

if __name__ == "__main__":
    print_specs()
