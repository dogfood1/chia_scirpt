# chia 维护中一些小脚本

## disk_info

fastapi 储存机信息 API

**启动方式**

uvicorn main:app --reload --host=192.168.1.55

## generate_mount.py

自动根据磁盘信息生成挂载信息

## generate_rsync.py

自动工具 disk_info 的磁盘信息生成 rsync 传输命令

## generate_wakeScirpt.py

用于根据磁盘挂在目录自动生成 wake_driver.sh

## wake_driver.sh

定时往硬盘写内容防止硬盘休眠 避免>50 问题
