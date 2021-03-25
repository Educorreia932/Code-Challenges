#!/bin/bash
repeat=$1
string=$2

for i in $(eval echo "{1..$repeat}")
do 
    echo -n $string
done    