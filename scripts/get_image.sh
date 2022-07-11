#!/bin/bash

WP_FILE=./wallpaper.jpg

bing="www.bing.com"

IMG_NUM=$(( $RANDOM % 10 ))

xmlURL="http://$bing/HPImageArchive.aspx?format=xml&idx=$IMG_NUM&n=1&mkt=en-US"

# Form the URL for the default pic resolution
defaultPicURL=$bing$(curl -s $xmlURL | grep -oP "(?<=<url>)(.*?)(?=</url>)")

curl -s -o "$WP_FILE" "$defaultPicURL"
