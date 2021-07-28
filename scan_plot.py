# -*-coding:utf-8-*- 
import os

listOfFilesToBeSynchronized = []
plotDirectoryPathList = []
for root,dirs,files in os.walk("/mnt/"): 
    for dir in dirs:
        pass
    for file in files:
        if ".plot" in os.path.join(root,file):
            path = os.path.join(root,file)
            if(os.path.splitext(path)[-1] == '.plot'):
                listOfFilesToBeSynchronized.append(path)


print(len(listOfFilesToBeSynchronized))
print(str((len(listOfFilesToBeSynchronized) *101 / 1024)) + 'TB')

for item in listOfFilesToBeSynchronized:
    print(item)
    plotDirectoryPathList.append(os.path.dirname(item))
    pass


plotDirectoryPathList = list({}.fromkeys(plotDirectoryPathList).keys())

for item in plotDirectoryPathList:
    print('chia plots add -d '+item)