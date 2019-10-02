# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:11:36 2019

@author: Ezxiio
"""

from itertools import chain
from nltk.corpus import wordnet

synonyms = wordnet.synsets("change")
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
print(set(chain.from_iterable([word.lemma_names() for word in synonyms])))