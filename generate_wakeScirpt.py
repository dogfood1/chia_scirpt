import os
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

if __name__ == '__main__':
    output = run_command('lsblk')
    output2 = run_command('blkid')
    diskInfo = getALLPolt(output,'sdr')

    for item in range(0,len(diskInfo[0])):
        print('screen -d -m -S chia'+str(item)+' bash -c \'while true; do date > '+diskInfo[0][item]+'/keep.awake; sleep 20; done\'')
