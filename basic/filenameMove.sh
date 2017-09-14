!#/bin/bash
# simple bash helper script for hanisch piana archive
# it searches for files and moves them dependend on their filename
# e.g. file: "D-DAI-HP-K12-z-001.jpg"
# script moves the file into "./Kasten 12/Zeichnung/"

find . -name "D-DAI*" | while read fname; do
  directory=$(echo $fname | cut -d"-" -f 6)
  type=$(echo $fname | cut -d"-" -f 5)
  if [ ${directory:0:1} = "K" ]; then
    directory="${directory//K/Kasten }"
  elif [ ${directory:0:1} = "M" ]; then
    directory="${directory//M/Mappe }"
  fi
  if [ $type = "f" ]; then
    subdir="Fotos"
  elif [ $type = "z" ]; then
    subdir="Zeichnungen"
  elif [ $type = "do" ]; then
    subdir="Dokumente"
  fi
  # check if directory exists, if not create it
  [ -d "$directory" ] || mkdir "$directory"
  [ -d "$directory/$subdir" ] || mkdir "$directory/$subdir"
  mv $fname "$directory/$subdir"
done
