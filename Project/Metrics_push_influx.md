import json
import os
import psutil
import time as t
import socket
from datetime import datetime
from influxdb import InfluxDBClient
client = InfluxDBClient("3.91.94.124", 8086, "admin", "admin")
value = client.get_list_database()
print(value)
client.switch_database('met_db')
c=0
while True:
    c+=1
    time=datetime.now()

    # HostName
    hostname = socket.gethostname()

        # Ip Addre
    IPAddr = socket.gethostbyname(hostname)

        # Cpu Info
    CPU_Pct=round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2)

        # Memory Usase
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = round(py.memory_info()[0]/2.**30,2)
    # Volume Usase
    def disk_stat(path):
        disk = os.statvfs(path)
        percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail) + 1
        return percent

    volume = disk_stat('/')

    json_body = [
        {
            "measurement": "metrics",
            "tags": {
                "user": "anand1",
            },
            "time": time,
            "fields": {
                "hos": hostname,
                                "ip": IPAddr,
                "cpu": CPU_Pct,
                "mem": memoryUse,
                "vol": volume
            }
        }
    ]
    client.write_points(json_body)
    t.sleep(2)
    if c==10000:
       break
