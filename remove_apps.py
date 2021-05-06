import os
with open('apps_to_remove.txt') as f:
    lines = f.readlines()
    for line in lines:
        os.system('adb shell pm uninstall -k --user 0 ' + line.strip())
