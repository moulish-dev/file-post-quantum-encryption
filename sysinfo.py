import platform
import psutil

def get_sysinfo():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "CPU Cores (Logical)": psutil.cpu_count(logical=True),
        "CPU Cores (Physical)": psutil.cpu_count(logical=False),
        "RAM Size (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Disk Size (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "Machine Type": platform.machine()
    }

    for key, value in system_info.items():
        print(f"{key}: {value}")

get_sysinfo()