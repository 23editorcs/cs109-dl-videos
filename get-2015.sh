#!/bin/bash

# To extract files:
# cat hd-2015-video-pages.txt | ./extract-2015.py > hd-video-files-2015.txt

# To downloaded extracted files:
# cat hd-2015-video-files.txt | ./get-2015.sh

#cat name.url.txt | while read line
#cat $1 | while read line
while read line
do
    echo $line
    name="`echo $line | cut -f1 -d,`.mp4"
    url="`echo $line | cut -f2 -d,`"
    echo "$name -> $url"
    wget $* -O "$name" "$url"
    #python2 add.py "$name" "$url"
    #aria2c $* -o "$name" "$url"
done
