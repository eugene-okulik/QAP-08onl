#!/bin/bash

word=""

while [[ $word != "." ]]
do
echo "Enter the word: "
read word
len=${#word}
if [[ $len -le 5 ]]
then echo "Ok"
else echo "The word is too long"
fi
done
