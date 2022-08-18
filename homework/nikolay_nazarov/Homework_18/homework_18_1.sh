#!/bin/bash

echo "Хотите установить Python? 1) Да 2) Нет"
read input
if [[ $input == "Да" ]]; then
    echo "Вы выбрали установить python"
    sleep 3
else
    echo "Все-равно установим"
    sleep 3
fi
