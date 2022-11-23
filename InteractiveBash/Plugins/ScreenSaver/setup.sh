sudo apt-get install libcurses-perl xprintidle -y
cd /tmp && wget http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/Term-Animation-2.4.tar.gz && tar -zxvf Term-Animation-2.4.tar.gz
cd Term-Animation-*/ && sudo perl Makefile.PL && sudo make && sudo make test && sudo make install
cd /tmp && wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz && tar -zxvf asciiquarium.tar.gz
cd asciiquarium_*/ && sudo cp asciiquarium /usr/local/bin && sudo chmod 0755 /usr/local/bin/asciiquarium

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

cd Plugins/ScreenSaver
echo "FILE="/tmp/interactive_screen_count"" >> $USERDIR/.bashrc
echo "if [[ -f /tmp/interactive_screen_count ]]; then" >> $USERDIR/.bashrc
echo "	if [[ \$(cat \$FILE 2>/dev/null) -gt 10 ]]; then" >> $USERDIR/.bashrc
echo "		rm /tmp/interactive_screen_count 2>/dev/null" >> $USERDIR/.bashrc
echo "		asciiquarium" >> $USERDIR/.bashrc
echo "	fi" >> $USERDIR/.bashrc
echo "	if [[ \$(cat \$FILE 2>/dev/null) -le 10 ]]; then" >> $USERDIR/.bashrc
echo "		sec_data=\$(cat \$FILE)" >> $USERDIR/.bashrc
echo "		rm /tmp/interactive_screen_count 2>/dev/null" >> $USERDIR/.bashrc
echo "		sec_data=\$(( \$sec_data + 1 ))" >> $USERDIR/.bashrc
echo "		echo "\$sec_data" > /tmp/interactive_screen_count" >> $USERDIR/.bashrc
echo "		" >> $USERDIR/.bashrc
echo "	fi" >> $USERDIR/.bashrc
echo "" >> $USERDIR/.bashrc
echo "else" >> $USERDIR/.bashrc
echo "	echo "0" > /tmp/interactive_screen_count" >> $USERDIR/.bashrc
echo "fi" >> $USERDIR/.bashrc
cd $1
