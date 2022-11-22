#! /bin/bash
location=$(greadlink -f "${BASH_SOURCE}") # this works for gnu coreutil package on mac, otherwise change to readlink
echo This script is located in $location
random=$RANDOM
echo Here\'s a random number for you
echo $random
echo Here is an alternative where a defined range is given and shuffled followed by output of one line:
shuf -i 1-100000 -n 1
read -p "Text input: " Text
echo $Text
