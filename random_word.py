#!/usr/bin/env python
from random import choice
from subprocess import Popen, PIPE
from pydoc import pager
with open("/Users/batur/vocabulary.md","r") as the_file:
    word = []
    while len(word) != 2:
        try:
            word = choice(the_file.readlines()).split("- ")
        except:
            pass
    word = word[1]
    print word

see_dict = raw_input("look it up? y or n:  ")
if see_dict.lower() == "y":
    process = Popen("~/Tools/script/trans -sp " + word,
                    shell=True,
                    stdout=PIPE,
                    stderr=PIPE,
                    executable='/bin/zsh')
    stdout, stderr = process.communicate()
    pager(stdout)



