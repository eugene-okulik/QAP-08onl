#!/bin/bash

text=""

while [[  $text != "."  ]]; do
      echo "Введите слово : "
      read text
      len=${#text}
if [[  $len -le 5  ]] && [[  $text != "."  ]]; then
      echo "ok"
elif [[  $len -ge 6  ]]; then
        echo "Слово слишком длинное"
fi
done 
