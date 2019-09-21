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

## Explanation
### What is that bruteforce thing?
- The first option (#1) takes to ciphertext and shifts all letters. A letter is shifted so that when it reaches the last english letter _z_ (the functions handles both lowercase and uppercase), the letter is resetted which means the next shift after _z_ will be _a_, then _b_ and so on until the last permutation (25th). Symbols are treated as they are, nothing changes.
- The second option (#2) takes the ciphertext and shifts all letters no matter what they are (assuming they are ASCII letters). When the ASCII code of a letters exceeds 255, it is resetted.

## Example
![Caesar's Cipher Decryption Tool Example](https://i.imgur.com/I43Ampr.png)
