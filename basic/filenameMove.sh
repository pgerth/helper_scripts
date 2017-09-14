!#/bin/bash
find . -name "D-DAI*" | while read fname; do
  directory=$(echo $fname | cut -d"-" -f 6)
  type=$(echo $fname | cut -d"-" -f 5)
  directory="${directory//K/Kasten }"
  if [ $type = "f" ]; then
    subdir="Foto"
  elif [ $type = "z" ]; then
    subdir="Zeichnung"
  fi
  echo "$directory/$subdir"
  # check if directory exists, if not create it
  [ -d "$directory" ] || mkdir "$directory"
  [ -d "$directory/$subdir" ] || mkdir "$directory/$subdir"
  mv $fname "$directory/$subdir"
done
