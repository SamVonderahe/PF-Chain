#!/bin/bash
artist=$(echo $1 | sed -r 's/ /%20/g')
rm final
touch final
wget \
\
\
\
\
\
-O $artist.html https://pitchfork.com/search/?query=$artist
grep -oP '\/reviews\/albums\/[^(\">)]*' $artist.html > links.html
while read -r line; do
    if [ ${#line} -gt 16 ]
      then
        echo $line
      fi
done < links.html > albums.html

declare -i num=1
while read -r line; do
  wget -O review$num.html pitchfork.com/$line;
  num=$((num + 1))
  sleep 0.5
done < albums.html

grep -oP "[^\"]* \| " review*.html > data
grep -oP "score\">[0-9].?[0-9]" review*.html >> data
grep -oP 'release_year\":[0-9]*' review*.html >> data
declare -i dup=0;
for (( i=1; i<$num; i++ ))
  do
    while read -r line; do
      if [[ "$line" == "review$i."* || $num -eq 2 ]]; then
        if [[ $dup -eq 0 ]]; then
          printf "E\n" >> final
          dup=1
        else
          echo $line | cut -f2- -d: | cut -f2- -d: >> final
        fi
      fi
    done < data
  dup=0
done

rm *.html
rm data
printf "\n$1:\n======================================\n"
#cat final
python graph.py
