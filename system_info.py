import platform
import psutil
import datetime
import json

def cpu_usage():
   return psutil.cpu_percent()

def memory_usage():
    return psutil.disk_usage('/')

def top_five_processes():
    processes = []

    for pr in psutil.process_iter(['pid']):
        proc = psutil.Process(pid=pr.pid)
        processes.append(proc.as_dict(attrs=['pid','name','username','cpu_percent','memory_percent']))
        processes = sorted(processes,key=lambda i: i['cpu_percent'],reverse = True)
    return processes



def network_statistics():
    pass

def system_uptime():
    boot_time= psutil.boot_time()
    boot_date_time = datetime.datetime.fromtimestamp(boot_time)
    return datetime.datetime.now() - boot_date_time

def gather_system_info_data():
    data =  {
                 "cpu_usage: ":cpu_usage(),
                 "memory_usage: ":memory_usage(),
                 "top_five_processes: ": top_five_processes(),
                 "network_statistics: ":network_statistics(),
                 "system_uptime: ":system_uptime()
            }
    return data