#!/bin/bash
# This script lists all saved Wi-Fi networks and their passwords, if available.
# 
# Usage:
#   bash wifi_grabber.sh

nmcli -g NAME,TYPE connection show | grep ':802-11-wireless' | cut -d: -f1 | while read -r wifi; do
    echo "SSID: $wifi"
    
    password=$(nmcli connection show "$wifi" | grep '802-11-wireless-security.psk:' | awk '{print $2}')
    
    if [[ -z "$password" || "$password" == "<hidden>" ]]; then
        echo "Password: [Not saved or protected]"
    else
        echo "Password: $password"
    fi

    echo
done
