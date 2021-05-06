#!/bin/bash

while read p; do
    adb shell pm uninstall -k --user 0 $p
done < apps_to_remove.txt
