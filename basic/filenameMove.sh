!#/bin/bash
# siple bash helper script for hanisch piana archive
# it searchs for files and moves them dependend on their filename
# e.g. file: "D-DAI-HP-K12-z-001.jpg"
# moves the file into "./Kasten 12/Zeichnung/"

find . -name "D-DAI*" | while read fname; do
  directory=$(echo $fname | cut -d"-" -f 6)
  type=$(echo $fname | cut -d"-" -f 5)
  directory="${directory//K/Kasten }"
  if [ $type = "f" ]; then
    subdir="Foto"
  elif [ $type = "z" ]; then
    subdir="Zeichnung"
  fi
  # check if directory exists, if not create it
  [ -d "$directory" ] || mkdir "$directory"
  [ -d "$directory/$subdir" ] || mkdir "$directory/$subdir"
  mv $fname "$directory/$subdir"
done
