#!/usr/bin/env python3


def main():
    """ Caesar's Cipher decryption tool """

    cipher = input("Enter the text to be decrypted > ").upper()
    blacklist_chars = r" ,./;'\"[]+=-_`!@#$%^&*(){}|:<>?"

    for i in range(1, 26):  # Iterate through the whole alphabet 
        decoded = ''
        for char in cipher:
            if char in blacklist_chars:     # if the current char is a symbol
                decoded += char             # copy it as it is
            elif (ord(char) + i) > 90:      # if the current char is lowercase
                decoded += chr(64 + (ord(char) + i) - 90)   # make it uppercase
            else:                           # if it's already uppercase
                decoded += chr(ord(char) + i)   # copy it as it is
        print("Round no. {0:2}: {1}".format(i, decoded))    # print the text
        # decrypted with all the keys => from 1 to 25 (26 is the text itself)


if __name__ == '__main__':
    main()  # Run it !
