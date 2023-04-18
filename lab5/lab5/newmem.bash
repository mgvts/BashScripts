#!/bin/bash

N=$1

list=()
count=0
rm "report.log" 2>/dev/null

while true;
do
        (( count += 1 ))
        list+=(1 2 3 4 5 6 7 8 9 10)
        if [[ $(( count*10 )) -eq $N ]]; then
                echo "newbash end $$ N = $N"
		exit
        fi 
done

