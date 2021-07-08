#!/bin/bash

read _
read -a numbers

(IFS=$'\n'; sort <<< "${numbers[*]}") | uniq -c
