import os
import requests

api_url = "http://192.168.1.55:8000"


def residualCapacity(elem):
    return elem[3]

# 获取存储机器磁盘剩余容量
def getStorageSpace():
    response = requests.get(api_url+'/system/diskInfo')
    storageSpace = response.json()
    storageSpace['disk'].sort(key=residualCapacity,reverse=True)
    return storageSpace['disk']

#获取当前机器储存容量
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
            diskInfo.append(tmp)

    return diskInfo

if __name__=='__main__':
    storageSpace = getStorageSpace()
    diskInfo = diskInfo()
    diskInfo.sort(key=residualCapacity)
    # print(diskInfo)
    for i in range(0,len(storageSpace)):
        # print(storageSpace[i][5])
        # print(diskInfo[i][5])
        rsync_command = 'rsync -vrtopg --progress -W --include "*.plot" --exclude="*.*" --preallocate --remove-source-files --skip-compress plot --whole-file ' + diskInfo[i][5] + ' chia@192.168.1.56:'+ storageSpace[i][5]
        print("screen -d -m -S rsync_"+str(i)+" bash -c '"+rsync_command+"'")
