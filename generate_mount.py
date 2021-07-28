import os 
from pathlib import Path

def run_command(command):
    output = os.popen(command)
    return output.read()

def notNone(item):
    return item != ''


def getALLPolt(output,systemDisk):
    tmp = output.split("\n")
    diskList = []
    for item in tmp:
        tmp1 = item.split(' ')
        tmp2 = filter(notNone, tmp1)
        diskList.append(list(tmp2))

    
    plotList = []
    newDisk = []
    diskCount = 0
    for item1 in diskList:
        if len(item1)> 0:
            if 'sd' in item1[0]:
                if '─' not in item1[0] and systemDisk not in item1[0]:
                    diskCount += 1

        if(len(item1) == 6):
            if '─' not in item1[0] and systemDisk not in item1[0]:
                newDisk.append(item1[0])
        else:
            if(len(item1)>6):
                if '/mnt/' in item1[6]:
                    plotList.append(item1[6])

        # print(item1)
        # plotList.append(item1[6])
    
    return(plotList,newDisk,diskCount)
            
def getAllDisk(output):
    tmp = output.split("\n")
    tmp1 = []
    for item in tmp:
        if '/dev/sd' in item:
            tmp1.append(item)
    
    return tmp1
             

if __name__ == '__main__':
    print("1:生成/etc/fstab,2:生成手动mount指令")
    generateType = input("请选择生成模式:")

    output = run_command('lsblk')
    output2 = run_command('blkid')
    diskInfo = getALLPolt(output,'sdr')
    diskIdList = getAllDisk(output2)

    tmpPlotList = []
    for pno in range(1,int(diskInfo[2])+1):
        pathUri = '/mnt/plot'+str(pno).zfill(2)
        tmpDir = Path(pathUri)
        if tmpDir.exists() == False:
            os.makedirs(pathUri)

        if pathUri not in diskInfo[0]:
            tmpPlotList.append(pathUri)
    
    
    
    
    print('剩余可用目录:'+str(len(tmpPlotList)),'实际未挂载硬盘:'+str(len(diskInfo[1])))
    
    
    for item in range(0,len(diskInfo[1])):
        # print(diskInfo[1][item])
        for item1 in diskIdList:
            if '/dev/'+diskInfo[1][item]+':' in item1:
                tmp = item1.split(' ')
                #print(tmpPlotList[item])
                #print(tmp[0])
                # print("mkdir "+tmpPlotList[item])

                if generateType == '2':
                    print('mount '+tmp[0].replace(":","")+" "+tmpPlotList[item])
                if generateType == '1':
                    print(tmp[0].replace('"','') + ' ' + tmpPlotList[item]+' '+tmp[2].replace('TYPE="','').replace('"','')+' defaults 0 0')

                
                
                
