import psutil
import json
from flask import jsonify
from flask import Flask

app = Flask(__name__)


@app.route('/')
def status():

 CpuDict  =  {
    'user':       int(psutil.cpu_times()[0]),
    'kernel':     int(psutil.cpu_times()[2]),
    'idle':       int(psutil.cpu_times()[3]),
    'iowait':     int(psutil.cpu_times()[4])
    }


 MemDict  =  {
    'total':      int(psutil.virtual_memory()[0]),
    'available':  int(psutil.virtual_memory()[1]),
    'percent':    int(psutil.virtual_memory()[2]),
    'used':       int(psutil.virtual_memory()[3]),
    'free':       int(psutil.virtual_memory()[4])
    }


 DiskDict =  {
    'total':      int(psutil.disk_usage('/')[0]),
    'used':       int(psutil.disk_usage('/')[1]),
    'free':       int(psutil.disk_usage('/')[2]),
    'percent':    int(psutil.disk_usage('/')[3])
    }


 CpuJson  =  json.dumps(CpuDict)
 MemJson  =  json.dumps(MemDict)
 DiskJson =  json.dumps(DiskDict)

 return jsonify(cpu=CpuJson, mem=MemJson, mounts=psutil.disk_partitions(), disk=DiskJson)
