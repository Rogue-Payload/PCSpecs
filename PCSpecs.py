import platform
import psutil
import GPUtil
import subprocess
from colorama import Fore, Style, init
import speedtest

# Initialize colorama for colored terminal output
init(autoreset=True)

def get_system_info():
    """
    Gathers general system information including OS, CPU, RAM, motherboard, and GPU.
    Returns:
        tuple: Contains OS info, CPU info, RAM size in GB, motherboard info, and GPU info.
    """
    os_info = platform.system() + " " + platform.release()
    cpu_info = get_cpu_info()
    ram_info = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    motherboard_info = get_motherboard_info()
    gpu_info = get_gpu_info()
    return os_info, cpu_info, ram_info, motherboard_info, gpu_info

def get_motherboard_info():
    """
    Retrieves the motherboard information for Windows and Linux systems.
    Uses command line tools and file reading to get the details.
    
    Returns:
        str: Motherboard manufacturer and model, or 'Unknown' if not found.
    """
    if platform.system() == "Windows":
        try:
            output = subprocess.check_output("wmic baseboard get product,Manufacturer", shell=True).decode()
            return output.split("\n")[1].strip()
        except Exception:
            return "Unknown"
    elif platform.system() == "Linux":
        try:
            # Reading motherboard details from the Linux file system
            with open('/sys/devices/virtual/dmi/id/board_vendor') as f:
                vendor = f.read().strip()
            with open('/sys/devices/virtual/dmi/id/board_name') as f:
                name = f.read().strip()
            return f"{vendor} {name}"
        except Exception:
            return "Unknown"
    return "Unknown"

def get_cpu_info():
    """Get detailed CPU information."""
    try:
        # Use lscpu command on Linux
        if platform.system() == "Linux":
            command = "lscpu | grep 'Model name'"
            result = subprocess.check_output(command, shell=True).decode()
            cpu_name = result.split(":")[1].strip() if ':' in result else "Unknown CPU"
        else:
            cpu_name = platform.processor()

        if not cpu_name:
            cpu_name = "Unknown CPU"
        
        cpu_cores = psutil.cpu_count(logical=True)
        cpu_physical_cores = psutil.cpu_count(logical=False)
        return f"{cpu_name} ({cpu_physical_cores} physical cores, {cpu_cores} logical cores)"
    except Exception as e:
        print(f"Could not retrieve CPU information: {e}")
        return "Unknown CPU"


def get_gpu_info():
    """Get GPU information with debugging."""
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            print(f"{Fore.GREEN}Detected GPU: {gpu.name} (Driver Version: {gpu.driver})")
            return f"{gpu.name} (Driver Version: {gpu.driver})"
        else:
            print(f"{Fore.RED}No GPU found with GPUtil.")
            return "No GPU found"
    except Exception as e:
        print(f"{Fore.RED}Error detecting GPU: {e}")
        return "No GPU found"


def get_internet_speed():
    """
    Measures the internet speed using the Speedtest library.
    
    Returns:
        str: Download, upload speeds and ping information, or an error message.
    """
    try:
        # Initializing the Speedtest and finding the best server
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        return f"Ping: {ping:.2f} ms, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps"
    except Exception as e:
        return f"Could not retrieve internet speed information: {e}"

def compare_specs_with_game(cpu, ram, gpu, game_name, game_specs):
    """
    Compares system specifications against a game's requirements.
    
    Args:
        cpu (str): The system's CPU information.
        ram (float): Total RAM in GB.
        gpu (str): The system's GPU information.
        game_name (str): The name of the game.
        game_specs (dict): The minimum, recommended, or high settings specs for the game.
    
    Returns:
        str: Status indicating if system exceeds, meets, or fails to meet requirements.
    """
    # Lowercase checks for case-insensitive matching of CPU and GPU models
    cpu_met = any(req_cpu.lower() in cpu.lower() for req_cpu in game_specs['cpu'])
    ram_met = ram >= game_specs['ram']
    gpu_met = any(req_gpu.lower() in gpu.lower() for req_gpu in game_specs['gpu'])
    
    # Determine the overall compatibility status based on individual checks
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
    """
    Prints out system specs and evaluates game compatibility.
    Compares against specific game requirements for accurate output.
    """
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
    internet_speed_info = get_internet_speed()
    print(f"{Fore.CYAN}{internet_speed_info}\n")

    # Game specs for comparison
    game_requirements = {
        "Call of Duty": {
            "cpu": ["i3-4340", "i5-2500K", "i7-8700K", "i7-9700K"],
            "ram": 16,  # Highest requirement among different versions
            "gpu": ["GTX 670", "GTX 970", "GTX 1080", "RTX 2070", "RTX 2080 SUPER"]
        },
        "Fortnite": {
            "cpu": ["i3-3225", "i5-7300U", "i7-8700"],
            "ram": 16,  # Highest requirement
            "gpu": ["HD 4000", "GTX 960", "RTX 3070"]
        },
        "Roblox": {
            "cpu": ["1.6 GHz", "Dual-core"],
            "ram": 4,  # Recommended requirement
            "gpu": ["DX10-compatible", "Dedicated GPU"]
        },
        "Minecraft": {
            "cpu": ["i3-4150", "i7-6500U", "FX-4100"],
            "ram": 8,  # Recommended requirement
            "gpu": ["HD 4400", "GeForce 940M", "HD 7750"]
        }
    }

    print(f"{Fore.BLUE}\nGame Compatibility Check:")
    for game_name, specs in game_requirements.items():
        status = compare_specs_with_game(cpu_info, ram_info, gpu_info, game_name, specs)
        print(f"{Fore.MAGENTA}{game_name}: {status}")

if __name__ == "__main__":
    # Main execution
    print_specs()
