apt install x11-xserver-utils sct -y

USER="`whoami`"
if [[ $USER != "root" ]]; then
        USERDIR="/home/`whoami`"
else
        USERDIR="/root"
fi

if [[ ! $(echo "$1" | awk -F '/' '{print $NF}') == "InteractiveBash" ]]; then
	exit
else
	cd $1
fi

cd Plugins/EyeProtect
	echo "\n" >> "$USERDIR""/.bashrc"
	echo "if [[ \`echo \"\$(date +%T)\"  | awk -F ':' '{print \$1*60*60+\$2*60+\$3}'\` -lt 68400 ]]; then " >> "$USERDIR""/.bashrc"
	echo "	xrandr --output LVDS-1 --brightness 1 && echo 10 | tee /sys/class/backlight/acpi_video0/brightness 1>/dev/null && sct 7500 " >> "$USERDIR""/.bashrc"
	echo "elif [[ \`echo \"\$(date +%T)\"  | awk -F ':' '{print \$1*60*60+\$2*60+\$3}'\` -lt 75600 ]]; then	" >> "$USERDIR""/.bashrc"
	echo "	xrandr --output LVDS-1 --brightness 0.80 && echo 2 | tee /sys/class/backlight/acpi_video0/brightness 1>/dev/null && sct 4000" >> "$USERDIR""/.bashrc"
	echo "else" >> "$USERDIR""/.bashrc"
	echo "	xrandr --output LVDS-1 --brightness 0.80 && echo 1 | tee /sys/class/backlight/acpi_video0/brightness 1>/dev/null && sct 2350" >> "$USERDIR""/.bashrc"
	echo "fi" >> "$USERDIR""/.bashrc"
cd $1
