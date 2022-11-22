#!/usr/bin/python3
import shutil
import time
import os

fail_log = []
file_size = 0
def read_file():
    shutil.copy2("/var/log/auth.log", "/var/log/auth.log2")
    with open("/var/log/auth.log2") as auth_log:
        for each in auth_log.readlines():
            if "failure" in each.lower() and each not in fail_log:
                fail_log.append(each)
                print(each)
                file_stats = os.stat("/var/log/auth.log")
                file_size = file_stats.st_size
                auth_log.close()
                return

while True:
    file_stat_check = os.stat("/var/log/auth.log")
    file_stat_size = file_stat_check.st_size
    if file_stat_size > file_size:
        read_file()
    time.sleep(360)
    continue

