#!/bin/sh
echo "しゃべりたくないお(´・ω・｀)\n"
say しゃべりたくないお
while true
do
  echo "[入力受付中]\n"
  read INPUT
  say $INPUT;

  if test $(($RANDOM % 5)) -eq 0 ; then
      echo "(｀・ω・´)\n"
    else
      echo "（´・ω・｀）\n"
      fi 
 
    echo "-----------------------"
done
