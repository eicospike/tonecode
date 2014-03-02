for x in $(cat $1); do
echo -en "\x$(echo -e "obase=16\n `echo -e "ibase=2\n $x"|bc`"|bc)"
done

