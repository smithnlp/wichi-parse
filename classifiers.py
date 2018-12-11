"""A script which reveals that these transcriptions (by a native speaker) of
Wichí are separating what have traditionally been considered bound morphemes as
stand-alone wordforms, including nominal possessive pronouns and classifiers.
"""
import re
import sys


def main():
    """Search for instances of nominal possessive pronouns and classifiers as
    spaced collocates rather than agglutinative morphemes. File by file, saving
    corresponding outputs.
    """
    infilename = sys.argv[1]

    justname = infilename.split('.')[0]

    outfilename = './' + justname + '.clsf'
    print(outfilename)

    with open(infilename, 'r') as f:
        intext = f.read().rstrip()

    with open(outfilename, 'w') as f:
        matches = re.findall(r'(\s\w*?\s+(?:o|na?|la|[l|t]ha|to|a)\s+?(?:ka|ko|lo)?\s?\w*?)\s', intext)  # noqa
        for m in matches:
            print(m, file=outfilename)  # noqa


if __name__ == '__main__':
    main()
