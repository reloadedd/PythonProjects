#!/usr/bin/env python3

import pdftotext
import argparse
import sys


def search_pdf(file, offset):
    """ Extract the legitimation codes from the PDF file and return them.

    :param file: the PDF file where to search
    :param offset: the column index
    :return: a list of all legitimation codes found
    """

    codes = []

    # Open the PDF file from where to search
    try:
        with open(file, "rb") as f:
            document = pdftotext.PDF(f)

            # Iterate through each page on the PDF file
            for pdf_page in document:
                pdf_lines = pdf_page.splitlines()
                for text_line in pdf_lines:
                    try:
                        codes.append(int(text_line.split()[-offset]))
                    # If the conversion fails because a word is being converted
                    # instead of a number, just skip it
                    except ValueError:
                        continue
                    # If that line doesn't contain a candidate, but something
                    # else
                    except IndexError:
                        continue
    except FileNotFoundError:
        print("[Error] The file doesn't exist or you don't have permission to"
              " read it.")
        sys.exit(-1)    # Exit the program

    return codes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search each contestant from "
                                     "<source_pdf> in <search_pdf>.")
    parser.add_argument("source_pdf", help="The PDF file from where to extract"
                                           " the values to be searched.")
    parser.add_argument("search_pdf", help="The PDF file where to search"
                                           " those values")
    parser.add_argument('offset', type=int, help="The column index, numbered "
                                                 "from right to left")
    args = parser.parse_args()

    # Make a list with all the contestants from the first PDF file
    contestants = search_pdf(args.source_pdf, args.offset)
    number_of_contestants = 0

    # Now that we have extracted the legitimation codes for every
    # contestant, we will compare that code against the codes from the other
    # PDF file that might contain them
    other_pdf = search_pdf(args.search_pdf, args.offset)
    for contestant in contestants:
        # print('[Debug] Trying ', contestant)
        if contestant in other_pdf:
            print("[Info] Contestant with legitimation code {:4} has been "
                  "found in {:4}".format(contestant, args.search_pdf))
            number_of_contestants += 1

    print("\n\tThe number of contestants found in both lists is",
          number_of_contestants)
