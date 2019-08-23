# What's this?
* A script to extract information from a PDF file and then compare it against another PDF file. The information is based on a column, whose index is entered as input (offset).

# Why would you ever need this?
* I used this to count how many contenders on an admission exam moved from waiting list to accepted list. Thus, it helped me to get an overview about the contenders "migration". The script has some level of generality, but it's purpose was particular. But I think it can be easily modified to solve similar problems. I could also do CTRL+C, CTRL+F, CTRL+V in browser for every contender in the list, or I could do this script.
* Disclaimer: This script it's not intended to be efficient, nor the most elegant one. ***It just works***

# How I use this?
* First, you need to install it's sole dependency, [pdftotext](https://github.com/jalan/pdftotext) (Installation instructions are there).  
* After that, you are ready to go! Use the script's help menu to guide you.
```
usage: main.py [-h] source_pdf search_pdf offset

Search each contestant from <source_pdf> in <search_pdf>.

positional arguments:
  source_pdf  The PDF file from where to extract the values to be searched.
  search_pdf  The PDF file where to search those values
  offset      The column index, numbered from right to left

optional arguments:
  -h, --help  show this help message and exit
```

# Example usage
```
$chmod u+x main.py
$./main.py L7_initial.pdf L4.pdf 4
[Info] Contestant with legitimation code  436 has been found in L4.pdf
[Info] Contestant with legitimation code 3207 has been found in L4.pdf
[Info] Contestant with legitimation code 3295 has been found in L4.pdf
[Info] Contestant with legitimation code  457 has been found in L4.pdf
[Info] Contestant with legitimation code 3584 has been found in L4.pdf
[Info] Contestant with legitimation code  341 has been found in L4.pdf
[Info] Contestant with legitimation code 1326 has been found in L4.pdf
[Info] Contestant with legitimation code 3400 has been found in L4.pdf
[Info] Contestant with legitimation code 3278 has been found in L4.pdf
[Info] Contestant with legitimation code 3167 has been found in L4.pdf
[Info] Contestant with legitimation code 3785 has been found in L4.pdf
[Info] Contestant with legitimation code 3176 has been found in L4.pdf
[Info] Contestant with legitimation code 3480 has been found in L4.pdf
[Info] Contestant with legitimation code  289 has been found in L4.pdf
[Info] Contestant with legitimation code 3673 has been found in L4.pdf
[Info] Contestant with legitimation code 3366 has been found in L4.pdf
[Info] Contestant with legitimation code 3585 has been found in L4.pdf
[Info] Contestant with legitimation code 3264 has been found in L4.pdf
[Info] Contestant with legitimation code 3375 has been found in L4.pdf
[Info] Contestant with legitimation code 3627 has been found in L4.pdf
[Info] Contestant with legitimation code 3060 has been found in L4.pdf
[Info] Contestant with legitimation code  674 has been found in L4.pdf
[Info] Contestant with legitimation code 3274 has been found in L4.pdf
[Info] Contestant with legitimation code 3413 has been found in L4.pdf
[Info] Contestant with legitimation code 3326 has been found in L4.pdf
[Info] Contestant with legitimation code 3200 has been found in L4.pdf
[Info] Contestant with legitimation code 3745 has been found in L4.pdf
[Info] Contestant with legitimation code 3831 has been found in L4.pdf
[Info] Contestant with legitimation code 3023 has been found in L4.pdf

	The number of contestants found in both lists is 29
```
