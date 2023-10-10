#!/bin/bash
tmp=$(cat /sys/class/thermal/thermal_zone0/temp)
tmp_threshold="60"

tmp_edited=$(($tmp/1000))

if [[ "$tmp_edited" -gt "$tmp_threshold" ]]; then
	echo "Teplota prekrocila $tmp_threshold stupnu! Aktualni teplota: $tmp_edited."
fi
