#!/usr/bin/env bash

string=$1

for (( i=${#string}; i >= 0; i-- )); do
    reversed=$reversed${string:$i:1}
done

echo $reversed
