#!/bin/bash

input=""

 while [[  $input != "."  ]]; do
       echo "Введите слово : "
       read input
       len=${#input}
 if [[  $len -le 5  ]]; then
       echo "OK"
 elif [[  $len -ge 6  ]]; then
         echo "Слово слишком длинное"
 fi
 done
