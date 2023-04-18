#!/bin/bash

n=$1

a=1
b=1

for ((i=1; i<$n; i++))
do
	if [[ $((i%2)) == 0 ]];then
		((a=a+b))
	else
		((b=a+b))
	fi
#	echo "a=$a b=$b"
done

#if [[ $((i%2)) == 0 ]];then
	#echo "a = $a"
#else
        #echo "b = $b" 
#fi

