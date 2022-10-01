#!/bin/bash

echo -n "input : ";
read input;
printf "\n"

if ((input % 2 == 0));
then
  let input=input-1;
fi

for ((angka=input; angka>0; angka=angka-2))
do
  echo $angka
done
