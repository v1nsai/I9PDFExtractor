# Imagemagick and Tesseract pipeline

#### Pre-requisites

###### Windows install

ImageMagick - https://www.imagemagick.org/script/download.php

Textcleaner script for ImageMagick (unix only) - http://www.fmwconcepts.com/imagemagick/textcleaner/index.php

Tesseract - https://github.com/tesseract-ocr/tesseract/wiki

###### Ubuntu install

```
sudo apt-get install imagemagick ghostscript tesseract-ocr
wget http://www.fmwconcepts.com/imagemagick/downloadcounter.php?scriptname=textcleaner&dirname=textcleaner
```
###### MacOS install

```
brew install imagemagick
brew install tesseract --all-languages
wget http://www.fmwconcepts.com/imagemagick/downloadcounter.php?scriptname=textcleaner&dirname=textcleaner
```

#### Converting and pre-processing

Convert the pdf into several PNGs, one for each page.  I've had best results at density=600, larger or smaller values don't seem to work as well.

`magick convert -density 600 -alpha remove bond_i9.pdf bond_i9.png`

(It's faster to work with a single page for now, once we're done experimenting we'll use the following to output a single multipage PNG)

`magick convert -density 600 -alpha remove i9.pdf -append i9%d.png`

Next we use the textcleaner script to brighten, increase contrast and fix orientation.  
These seem to be the optimal values for `-f` and `-t` but maybe there are other combinations

`./textcleaner -g -e stretch -f 10 -o 5 -t 10 -u bond_i9-0.png textclean_i9.png`

#### Scanning with Tesseract

Run it through Tesseract and output an HOCR file, which is basically HTML

`tesseract -l eng bond_i9-0.png bond.html hocr`