#! /bin/bash
location=$(greadlink -f "${BASH_SOURCE}") # this works for gnu coreutil package on mac, otherwise change to readlink
echo This script is located in $location
random=$RANDOM
echo Here\'s a random number for you
echo $random
read -p "Text input: " Text
echo $Text