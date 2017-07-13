import shutil
import time

while True:
    shutil.copyfile("C:\\Users\\raev_e\\Downloads\\dump", "C:\\Users\\raev_e\\Downloads\\dump_back")
    time.sleep(60)
    print time.time(), "OK"