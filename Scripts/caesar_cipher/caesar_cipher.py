#!/usr/bin/env python3
# Release Version: v1.1
# Author: rel0adedd

import argparse
import sys
from colorama import Fore

SCREEN = sys.stdout


def decrypt(ciphertext: str, force: int) -> None:
    """ Caesar's Cipher decryption tool
    This one deals with the text that will be printed on the screen."""

    if force == 1:
        for i in range(1, 26):  # Iterate through the whole english alphabet
            decoded = ''
            for char in ciphertext:
                if not char.isalpha():     # if the current char is a symbol
                    decoded += char             # or number, copy it as it is
                elif char.islower():    # If it's lowercase
                    value = ord(char) + i
                    if value > 122:
                        value = value % 122 - 1 + 97
                    decoded += chr(value)
                elif char.isupper():     # If it's uppercase
                    value = ord(char) + i
                    if value > 90:
                        value = value % 90 - 1 + 65
                    decoded += chr(value)

            print(Fore.RED, end='')
            print('Round no.', Fore.RESET, '{0:2}: {1}'.format(i, decoded))
    else:
        for i in range(1, 256):
            decoded = ''
            for char in cipher:
                value = ord(char) + i

                if value > 255:
                    value %= 256
                decoded += chr(value)

            print(Fore.RED, end='')
            print('Round no.', Fore.RESET, '{0:3}: {1}'.format(i, decoded))


def decrypt_into_file(ciphertext: str, force: int, write_here: str) -> None:
    """ Caesar's Cipher decryption tool
    This one deals with the text that will be saved on a file."""

    # Use the same var for opening the file
    write_here = open(write_here, 'w')

    if force == 1:
        for i in range(1, 26):  # Iterate through the whole english alphabet
            decoded = ''
            for char in ciphertext:
                if not char.isalpha():     # if the current char is a symbol
                    decoded += char             # or number, copy it as it is
                elif char.islower():    # If it's lowercase
                    value = ord(char) + i
                    if value > 122:
                        value = value % 122 - 1 + 97
                    decoded += chr(value)
                elif char.isupper():     # If it's uppercase
                    value = ord(char) + i
                    if value > 90:
                        value = value % 90 - 1 + 65
                    decoded += chr(value)

            print('Round no. {0:2}: {1}'.format(i, decoded), file=write_here)
    else:
        for i in range(1, 256):
            decoded = ''
            for char in cipher:
                value = ord(char) + i

                if value > 255:
                    value %= 256
                decoded += chr(value)

            print('Round no. {0:3}: {1}'.format(i, decoded), file=write_here)

    # Clean up
    write_here.close()


if __name__ == '__main__':
    # Prepare the parser
    parser = argparse.ArgumentParser(
        description="Caesar's Cipher Decryption Tool for CTFs (mostly)",
        formatter_class=argparse.RawTextHelpFormatter)

    # Configuring arguments
    # It's not my fault for those strange-looking strings, sorry...
    parser.add_argument('-m',
                        '--mode',
                        type=int,
                        choices=(1, 2, 3),
                        default=1,
                        help='''[1] - Take data from stdin (you will be \
prompted to enter it)
[2] - Take data from a command-line argument --> [-c] option
[3] - Take data from a file given as argument with the [-f] option
Note: Default is 1.''')
    parser.add_argument('-b',
                        '--bruteforce',
                        type=int,
                        choices=(1, 2),
                        default=1,
                        help='''[1] - Brute-force ASCII English letters \
(26 combinations)
[2] - Brute-force ASCII Extended (256 combinations)
Note: Default is 1.''')
    parser.add_argument('-f',
                        '--file',
                        help='''The file that stores the ciphertext.
Required if mode is set to #3.''')
    parser.add_argument('-c',
                        '--ciphertext',
                        help='''The ciphertext to be decrypted.
Required if mode is set to #2.''')
    parser.add_argument('-o',
                        '--output',
                        help='The output file to write to.',
                        default=SCREEN)     # Print on the screen
    # Parse the arguments
    args = parser.parse_args()

    try:
        cipher = ''
        if args.mode == 1:
            cipher = input('c1ph3rt3xt [>>>] ')
        elif args.mode == 2:
            cipher = args.ciphertext

            if not cipher:
                print(Fore.YELLOW)
                print('If you use mode #2, you need to pass the ciphertext '
                      'with -c')
                print(Fore.RESET)
                parser.print_usage()
                sys.exit(-1)
        elif args.mode == 3:
            try:
                with open(args.file) as crack_me_file:
                    # Put the whole file into a variable
                    # I'm aware that this is not the best idea I've ever had
                    # If you wanna put a 10 gb file into memory, do it!
                    # But I won't do this on a CTF.
                    cipher = crack_me_file.read()
            except TypeError:
                print(Fore.YELLOW)
                print('If you use mode #3, you need to pass a file with -f')
                print(Fore.RESET)
                parser.print_usage()
                sys.exit(-1)

        if args.output != SCREEN:
            decrypt_into_file(cipher, args.bruteforce, args.output)
        else:
            decrypt(cipher, args.bruteforce)
    except KeyboardInterrupt:
        print("\n\tI know you'll come back to me (^-^)")
