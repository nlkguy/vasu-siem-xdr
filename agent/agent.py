# vasu - agent.py
# author - nlkguy
# /agent/agent.py

import psutil , platform , datetime , socket


def sysinfo():
    uname = platform.uname()
    svmem = psutil.virtual_memory()._asdict()
    swap = psutil.swap_memory()._asdict()
    return {
        "hostname": uname.node,
        "os": uname.system,
        "os_version": uname.version,
        "kernel": uname.release,
        "architecture": uname.machine,
        "processor": uname.processor,
        "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": socket.gethostbyname(socket.gethostname()),

        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else {},
        "cpu_percent": psutil.cpu_percent(interval=1),
        "per_cpu_percent": psutil.cpu_percent(interval=1, percpu=True),
        "load_avg": psutil.getloadavg() if hasattr(psutil, "getloadavg") else None,
        "virtual_memory": svmem,
        "swap_memory": swap,
        
    }

print(sysinfo())