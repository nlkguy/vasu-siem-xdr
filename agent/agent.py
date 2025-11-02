# ============================================
# vasu - agent.py
# author - nlkguy
# /agent/agent.py
# ============================================

import psutil , platform , os
# https://github.com/giampaolo/psutil
# https://www.askpython.com/python-modules/python-platform-module
import socket , requests
import threading , subprocess
# todo multithreading
import hashlib , uuid , time , json
# ✅ ⚠️ ❌ 💀
from datetime import datetime


VASU_SERVER = "http://localhost:8000/ingest"
AGENT_VERSION = "1.0.3"
HEARTBEAT_INT = 10 # def

#todo - add env/ os env variable/file
#todo - 
#todo - 
#todo - 

def gen_uuid():
    """generate/retrieve persistent uuid."""
    path = os.path.join(os.path.expanduser("~"), ".vasu_id")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()

    uid = str(uuid.uuid4())
    with open(path, "w") as f:
        f.write(uid)
    return uid

def get_sysinfo():
    """get sysinfo - host"""
    uname = platform.uname()
    return {
        "hostname": uname.node,
        "uuid": gen_uuid(),
        "os_name": uname.system,
        "os_version": uname.release,
        "architecture": uname.machine,
        "uptime_seconds": int(time.time() - psutil.boot_time()),
        "agent_version": AGENT_VERSION
    }

def get_usage():
    """get usage data on CPU,Mem,Disk(s)"""
    try:
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        disk = psutil.disk_usage('/')
        load_avg = os.getloadavg() if hasattr(os, 'getloadavg') else (0, 0, 0)

        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "cpu_cores": psutil.cpu_count(logical=True),
            "load_avg_1m": load_avg[0],
            "load_avg_5m": load_avg[1],
            "load_avg_15m": load_avg[2],
            "memory_total_mb": memory.total / (1024 * 1024),
            "memory_used_mb": memory.used / (1024 * 1024),
            "memory_percent": memory.percent,
            "swap_used_mb": swap.used / (1024 * 1024),
            "swap_percent": swap.percent,
            "disk_total_gb": disk.total / (1024 ** 3),
            "disk_used_gb": disk.used / (1024 ** 3),
            "disk_percent": disk.percent,
        }
    except Exception as e:
        return {"error": f"resource_usage: {str(e)}"}

def get_nwinfo():
    """get n/w info,connections,stats."""
    try:
        addrs = psutil.net_if_addrs()
        stats = psutil.net_io_counters()
        connections = psutil.net_connections()
        interfaces = {}

        for iface, addr_list in addrs.items():
            ip_addrs = [a.address for a in addr_list if a.family == socket.AF_INET]
            mac_addrs = [a.address for a in addr_list if a.family in (socket.AF_PACKET, getattr(socket, 'AF_LINK', None))]
            interfaces[iface] = {
                "ip": ip_addrs,
                "mac": mac_addrs,
            }

        return {
            "interfaces": interfaces,
            "bytes_sent": stats.bytes_sent,
            "bytes_recv": stats.bytes_recv,
            "packets_sent": stats.packets_sent,
            "packets_recv": stats.packets_recv,
            "active_connections": len(connections),
        }
    except Exception as e:
        return {"error": f"network_info: {str(e)}"}

def get_procinfo(max_processes=10):
    """get top running processses info."""
    processes = []
    try:
        for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
            try:
                info = p.info
                processes.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        # sort by mem usage
        processes = sorted(processes, key=lambda x: x.get('memory_percent', 0), reverse=True)[:max_processes]
        return processes
    except Exception as e:
        return [{"error": f"process_info: {str(e)}"}]


def get_battinfo():
    """get battery info if present."""
    try:
        battery = psutil.sensors_battery()
        if not battery:
            return {}
        return {
            "percent": battery.percent,
            "plugged_in": battery.power_plugged,
            "time_left_mins": None if battery.secsleft == psutil.POWER_TIME_UNLIMITED else int(battery.secsleft / 60)
        }
    except Exception as e:
        return {"error": f"battery_info: {e}"}



def get_userinfo():
    """get active user(s) info."""
    try:
        users = []
        for u in psutil.users():
            users.append({
                "name": u.name,
                "terminal": u.terminal,
                "host": u.host,
                "started": datetime.fromtimestamp(u.started).isoformat(),
            })
        return users
    except Exception as e:
        return [{"error": f"user_info: {str(e)}"}]



def summary_all():
    """aggregate all data into payload with ts"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "system": get_sysinfo(),
        "resources": get_usage(),
        "network": get_nwinfo(),
        "users": get_userinfo(),
        "processes": get_procinfo(),
        "battery": get_battinfo(),
    }
    return data



def to_server(data, server_url="http://127.0.0.1:8000/ingest"):
    """send payload to server"""
    try:
        r = requests.post(server_url, json=data, timeout=5)
        if r.status_code == 200:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Sent payload.")
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠️ Server status {r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error sending: {e}")



def main():
    """periodic collection."""
    print("VASU collecting telemetry...")
    # env todo/-
    SERVER_URL = os.getenv("VASU_SERVER", "http://127.0.0.1:8000/ingest")
    INTERVAL = int(os.getenv("VASU_INTERVAL", str(HEARTBEAT_INT)))

    while True:
        payload = summary_all()
        to_server(payload, SERVER_URL)
        time.sleep(INTERVAL)



if __name__ == "__main__":
    main()


"""
if __name__ == "__main__":
    main()

    
    - heartbeat todo/
    - multithreading/
    -


print(get_sysinfo())
print("============================================")
print(get_usage())
print("============================================")
print(get_nwinfo())
print("============================================")
print(get_procinfo())
print("============================================")
print(get_battinfo())
print("============================================")
print(get_userinfo())
print("============================================")

"""