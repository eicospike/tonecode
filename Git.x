#!/bin/bash
#better have pulled first so pull
#and usage should give a check for commit name :)
if [ -z "$1" ]
   then
	echo "usage: Git {commit message}" && exit
fi


echo $2
if [ "$2" ]
	then
		echo "**********idk why you put a space in*************\n***************************************************"
fi
echo "##################CLEANING UP SORRY############################"
#rm ./Bin/*
#rm ./data/*


git add -A
git commit -m "$1"
git push origin master
