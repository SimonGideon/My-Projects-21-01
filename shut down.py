import os
shutdown = input("Do you want to shut down?(yes(1) or NO(0):")
if shutdown == ('No','0'):
    exit()
else:
    os.system("shutdown/s/t i")