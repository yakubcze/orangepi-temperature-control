#!/bin/bash
tmp=$(cat /sys/class/thermal/thermal_zone0/temp)

tmp_edited=$(($tmp/1000))
echo "Aktualni teplota: $tmp_edited."

