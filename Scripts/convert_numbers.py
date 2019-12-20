#!/usr/bin/env python3

import argparse


def convert_binary_to_int(number: str) -> int:
    """Return the decimal representation of an integer."""
    return int(number, 2)


def convert_hex_to_int(number: str) -> str:
    """Return the decimal representation of a hexadecimal number."""
    return str(int(number, 16))


def convert_int_to_hex(number: str) -> str:
    """Return the hexadecimal representation of an integer."""
    try:
        number = int(number)
    except ValueError:
        return '[Error]: The input was not a number!'

    return hex(number)


def convert_binary_to_hex(number: str) -> str:
    """Return the hexadecimal representation of a binary number."""
    return hex(convert_binary_to_int(number))


def convert_int_to_binary(number: str) -> str:
    """Return the binary representation of a number."""
    try:
        number = int(number)
    except ValueError:
        return '[Error]: The input was not a number!'

    return bin(number)[2:]  # Eliminate the '0b' prefix


def convert_hex_to_binary(number: str) -> str:
    """Return the binary representation of a hexadecimal number."""
    return convert_int_to_binary(convert_hex_to_int(number))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert numbers to different'
                                                 ' representations (bases)')
    parser.add_argument('mode',
                        help='The way in which a number should be converted. '
                             'e.g: bti = Binary To Int / htb = Hex To Binary',
                        choices=['bti', 'hti', 'ith', 'bth', 'itb', 'htb'])
    parser.add_argument('number',
                        help='The number to be converted to another base')
    args = parser.parse_args()

    if args.mode == 'bti':
        print(convert_binary_to_int(args.number))
    elif args.mode == 'hti':
        print(convert_hex_to_int(args.number))
    elif args.mode == 'ith':
        print(convert_int_to_hex(args.number))
    elif args.mode == 'bth':
        print(convert_binary_to_hex(args.number))
    elif args.mode == 'itb':
        print(convert_int_to_binary(args.number))
    else:
        print(convert_hex_to_binary(args.number))
