#!/usr/bin/env python3

"""A tool for batch morphological analysis of Wichi words."""

from collections import defaultdict as dd
import subprocess
import sys

import pandas as pd
from progress.bar import IncrementalBar
from pprint import pprint


def main():

    morpho_data = dd(list)

    infilename = sys.argv[1]
    justname = infilename.split('.')[0]
    outfilename = justname + '.out'
    with open(infilename, 'r') as f:
        intext = f.read().rstrip()

    tokens = intext.split(' ')

    outf = open(outfilename, 'w')

    bar = IncrementalBar('Processing token by token', max=len(tokens),
                         suffix='%(percent).1f%% |')

    for t in tokens:
        bar.next()

        proc1 = subprocess.Popen(['echo', t.lower()],
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True)
        proc2 = subprocess.Popen(['flookup', 'wichi.bin'],
                                 stdin=proc1.stdout,
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True)
        for item in proc2.stdout:
            outf.write(item)
            morpho_data[t] = item

        df = pd.DataFrame(morpho_data, index=[0])
        pprint(df)

    bar.finish()
    outf.close()


if __name__ == '__main__':
    main()
