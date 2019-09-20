# Caesar's Cipher Decryption Tool for CTFs (mostly)
## Description
This tool is meant to be used for CTF competitions (where else could you find Caesar's Cipher?), but don't listen to me, use it where you want! I made it to be flexible enough, depending on your situation.

## Requirements
- *Colorama*  
```pip3 install colorama```

## Usage
```
usage: caesar_cipher.py [-h] [-m {1,2,3}] [-b {1,2}] [-f FILE] [-c CIPHERTEXT]
                        [-o OUTPUT]

Caesar's Cipher Decryption Tool for CTFs (mostly)

optional arguments:
  -h, --help            show this help message and exit
  -m {1,2,3}, --mode {1,2,3}
                        [1] - Take data from stdin (you will be prompted to enter it)
                        [2] - Take data from a command-line argument --> [-c] option
                        [3] - Take data from a file given as argument with the [-f] option
                        Note: Default is 1.
  -b {1,2}, --bruteforce {1,2}
                        [1] - Brute-force ASCII English letters (26 combinations)
                        [2] - Brute-force ASCII Extended (256 combinations)
                        Note: Default is 1.
  -f FILE, --file FILE  The file that stores the ciphertext.
                        Required if mode is set to #3.
  -c CIPHERTEXT, --ciphertext CIPHERTEXT
                        The ciphertext to be decrypted.
                        Required if mode is set to #2.
  -o OUTPUT, --output OUTPUT
                        The output file to write to.
```

## Example
![Caesar's Cipher Decryption Tool Example](https://imgur.com/a/mL80II2)
