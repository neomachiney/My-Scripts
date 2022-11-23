# LINK
addbinary ()
{
    if [[ "$2" == "" ]]; then
        chmod +x `pwd`"/""$1" && ln -nsf `pwd`"/""$1" /root/NeoMachine/My-Tools/MyBinaries/$2;
    else
        chmod +x `pwd`"/""$1" && ln -nsf `pwd`"/""$1" /root/NeoMachine/My-Tools/MyBinaries/$2;
    fi
}

cat PYLINK | while read LINK_PY
do
	(cd "$LINK_PY" && addbinary "$LINK_PY.py" "$LINK_PY")
done
