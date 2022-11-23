apt install cowsay xcowsay toilet fortune lolcat -y 
apt install imagemagick x11-apps figlet -y
apt install sudo wget python3 cmatrix oneko neofetch -y

USER="`whoami`"
if [[ $USER != "root" ]]; then
        USER="/home/`whoami`"
else
        USER="/root"
fi

if [[ ! $(echo "$1" | awk -F '/' '{print $NF}') == "InteractiveBash" ]]; then
	exit
else
	cd $1
fi

cd Plugins/ColorfulTerminal 
# reformatting must be done
: '
echo "export PATH=/usr/games:\$PATH" >> $USER/.bashrc 
echo "COWPATH=\"`pwd`\"\"/\"" >> $USER/.bashrc 
echo "COWPATH=\"\$COWPATH\"\"Cowsay.py\"" >> $USER/.bashrc 
echo "random=\$(od -An -N4 -i < /dev/urandom) " >> $USER/.bashrc 
echo "" >> $USER/.bashrc 
echo "if [ \$(( \$random % 5 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $USER/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 2 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "		RANDOM2=\$RANDOM" >> $USER/.bashrc 
echo "		if [ \$(( \$RANDOM2 % 3 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "			python3 \"\$COWPATH\"" >> $USER/.bashrc 
echo "			echo" >> $USER/.bashrc 
echo "		elif [ \$(( \$RANDOM2 % 3 )) -eq 1 ]; then " >> $USER/.bashrc 
echo "			python3 \"\$COWPATH\"" >> $USER/.bashrc 
echo "			oneko 1>/dev/null 2>/dev/null &" >> $USER/.bashrc 
echo "			echo	" >> $USER/.bashrc 
echo "		elif  [ \$(( \$RANDOM2 % 3 )) -eq 2 ]; then " >> $USER/.bashrc 
echo "			python3 \"\$COWPATH\" | lolcat" >> $USER/.bashrc 
echo "			echo" >> $USER/.bashrc 
echo "		fi" >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 2 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "		RANDOM2=\$RANDOM" >> $USER/.bashrc 
echo "		if [ \$(( \$RANDOM2 % 3 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "			xcowsay \"Text\"" >> $USER/.bashrc 
echo "			echo" >> $USER/.bashrc 
echo "		elif [ \$(( \$RANDOM2 % 3 )) -eq 1 ]; then " >> $USER/.bashrc 
echo "			xcowsay \"Text\"" >> $USER/.bashrc 
echo "			xeyes 1>/dev/null 2>/dev/null &" >> $USER/.bashrc 
echo "			echo	" >> $USER/.bashrc 
echo "		elif  [ \$(( \$RANDOM2 % 3 )) -eq 2 ]; then " >> $USER/.bashrc 
echo "			fortune | xcowsay" >> $USER/.bashrc 
echo "			echo" >> $USER/.bashrc 
echo "		fi" >> $USER/.bashrc 
echo "	fi " >> $USER/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 2 ]; then" >> $USER/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $USER/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 2 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "		fortune" >> $USER/.bashrc 
echo "		echo " >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 2 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "		fortune | lolcat" >> $USER/.bashrc 
echo "		timeout 300 oneko -dog 1>/dev/null 2>/dev/null &" >> $USER/.bashrc 
echo "		echo " >> $USER/.bashrc 
echo "	fi" >> $USER/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 3 ]; then" >> $USER/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $USER/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 2 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "		neofetch" >> $USER/.bashrc 
echo "		echo " >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 2 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "		neofetch | lolcat" >> $USER/.bashrc 
echo "		echo" >> $USER/.bashrc 
echo "	fi" >> $USER/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 4 ]; then" >> $USER/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $USER/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 3 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "		RANDOM2=\$RANDOM" >> $USER/.bashrc 
echo "		if [ \$(( \$RANDOM2 % 2 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "			timeout 10 cmatrix -bos" >> $USER/.bashrc 
echo "			echo" >> $USER/.bashrc 
echo "		elif [ \$(( \$RANDOM2 % 2 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "			timeout 10 cmatrix -ns -C red" >> $USER/.bashrc 
echo "		fi" >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 3 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "		timeout 10 cmatrix -s | lolcat" >> $USER/.bashrc 
echo "		echo " >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 3 )) -eq 2 ]; then " >> $USER/.bashrc 
echo "		timeout 10 cmatrix -as -C blue" >> $USER/.bashrc 
echo "		oneko -sakura 1>/dev/null 2>/dev/null &" >> $USER/.bashrc 
echo "	fi" >> $USER/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $USER/.bashrc 
echo "	toilet_array=(\`ls /usr/share/figlet | xargs\`)" >> $USER/.bashrc 
echo "	TOILET=\$(( \$RANDOM % \${#toilet_array[@]} ))" >> $USER/.bashrc 
echo "	toilet_font=\${toilet_array[\$TOILET]}" >> $USER/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 4 )) -eq 0 ]; then" >> $USER/.bashrc 
echo "		toilet -f \$toilet_font -F gay \"Text\"" >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 4 )) -eq 1 ]; then" >> $USER/.bashrc 
echo "		toilet -f \$toilet_font \"Text\"" >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 4 )) -eq 2 ]; then" >> $USER/.bashrc 
echo "		toilet -f \$toilet_font -F border \"Text\"" >> $USER/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 4 )) -eq 3 ]; then" >> $USER/.bashrc 
echo "		toilet -F metal	-f \$toilet_font" >> $USER/.bashrc 
echo "	fi " >> $USER/.bashrc 
echo "fi" >> $USER/.bashrc 
echo "disown -a" >> $USER/.bashrc 
'
cd $1
