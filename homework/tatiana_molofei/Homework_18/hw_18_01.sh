#!/bin/bash

PS3='Хотите установить Python?'

select variants in Yes No
do
case $variants in
Yes) echo 'Вы выбрали установить python'
No) echo 'Все-равно установим'
esac

done
