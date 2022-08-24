#!/bin/bash

PS3="Хотите установить Python?"
echo
select choice in "Да" "Нет"
do
if [[ $choice == "Да" || "1" ]]
then echo "Вы выбрали установить Python"
break
else echo "Все равно установим"
break
fi
done
echo "Cпасибо, что сделали правильный выбор"
