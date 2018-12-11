## Wichí Parser

Instructions for how to update, compile, and use the foma-based morphological parser for Wichí.

#### 1. Make changes to wichi.lexc and/or wichi.foma

#### 2. Recompile the transducer and save it to an executable
```
$ foma
foma[0]: source wichi.foma
foma[1]: save stack wichi.bin
```
#### 3. Process text files of Wichí, saving them to corresponding output files.

For batch processing:
```
$ for each in manuscripts/*.txt; do python3 morphoprocess.py ${each}; done
```
For one file:
```
$ python3 morphoprocess.py manuscripts/inputfile.txt
```

#### TODO
- [x] create repo with all current work
- [x] adjust the output of morphoprocess.py (pandas dataframe, pickled)
- [ ] write foma rules tuned to laureano's data

#### LINKS
  * [foma morphology tutorial](https://fomafst.github.io/morphtut.html)
  * [foma intro](https://github.com/mhulden/foma/blob/master/foma/docs/simpleintro.md)
  * [textbook of Wichí](http://lenguawichi.com.ar/wp-content/uploads/2017/01/manual-gramatica-wichi-vol-1.original.pdf)
  * [dictionary of Wichí](http://www.languageconservation.org/images/Test/wichi%20dictionary_1.pdf)
