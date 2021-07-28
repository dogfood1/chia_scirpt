from typing import Optional
from fastapi import FastAPI
import uvicorn
import os
import subprocess

app = FastAPI()


def notNone(item):
    return item != ''

@app.get("/")
def read_root():
    return {"version": "1.0.0"}



@app.get('/system/diskInfo')
def diskInfo():
    diskml = 'df -hBG|sed \'1d;/ /!N;s/\\n//;s/ \\+/ /;\''
    # diskml = 'ps -ef |grep rysnc'
    output = os.popen(diskml).read()
    diskInfo = []
    for item in output.split("\n"):
        if "/mnt/plot" in item:
            tmp = []
            for item2 in item.split(' '):
                if item2 != '':
                    tmp.append(item2)

            tmp[1] = int(tmp[1].replace('G', ''))
            tmp[2] = int(tmp[2].replace('G', ''))
            tmp[3] = int(tmp[3].replace('G', ''))
            tmp[4] = int(tmp[4].replace('%', ''))
            if tmp[3] > 110:
                diskInfo.append(tmp)

    return {"disk":diskInfo}

@app.get('/system/physicalHardDisk')
def physicalHardDiskInfo():
    output = os.popen('lsblk').read()
    diskInfo = []
    for item in output.split("\n"):
        if 'sd' in item:
            if '─' not in item:
                diskInfo.append(item)
    return {'disk':diskInfo}
