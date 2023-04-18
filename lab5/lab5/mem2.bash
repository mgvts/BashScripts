#!/bin/bash

list=()
count=0
rm "report2.log" 2>/dev/null

while true;
do
        (( count += 1 ))
        list+=(1 2 3 4 5 6 7 8 9 10)
        if [[ $(( count % 100000 )) == 0 ]]; then
                echo "$((count * 10))" >> "report2.log"  
        fi 
done




