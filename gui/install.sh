cp ./www /
cp ./usr /
chmod +x /www/cgi-bin/*

PASSEXISTED = `grep -c "sys_pass" "/etc/drcom.conf"`
if [ $PASSEXISTED != "0" ]
    then
    echo "sys_pass = \"123456\"" >> /etc/drcom.conf
fi

