#!/bin/bash

word=""

while [[$word != "."]]; do
echo "Enter any word: "
read word
len=${#word}
if [[$len -le 5]]; then
echo "ok"
elif [[[$len -ge 5]]; then
echo "The word is too long"
fi
done

