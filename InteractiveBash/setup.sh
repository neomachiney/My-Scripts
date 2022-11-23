DIRNAME="InteractiveBash"
CURRENT="`pwd`"

if [[ $# -eq 0 ]]; then
	USER="`whoami`"
	if [[ $USER != "root" ]]; then
		USERDIR="/home/`whoami`"
	else
		USERDIR="/root"
	fi

	mkdir "$USERDIR""/.bash_interactive/backup" -p
	cp "$USERDIR""/.bashrc" "$USERDIR""/.bash_interactive/backup/.bashrc"
	cd .. && cp InteractiveBash/ ~/.bash_interactive/ -r
	bash "$USERDIR""/.bash_interactive/InteractiveBash/setup.sh" $USERDIR 
fi

if [[ $# -eq 1 ]]; then
	CURRENTDIR="$1""/.bash_interactive/InteractiveBash/"
	cd $CURRENTDIR || exit

	#Plugin No 1. ColorfulTerminal 
	chmod +x Plugins/ColorfulTerminal/setup.sh
	bash Plugins/ColorfulTerminal/setup.sh $CURRENTDIR

	#Plugin No 2. Screensaver
	chmod +x Plugins/ScreenSaver/setup.sh
	bash Plugins/ScreenSaver/setup.sh $CURRENTDIR

	#Plugin No 3. EyeProtect
	chmod +x Plugins/EyeProtect/setup.sh
	bash Plugins/EyeProtect/setup.sh $CURRENTDIR
fi
