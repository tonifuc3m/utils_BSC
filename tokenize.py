#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:12:53 2021

@author: antonio
"""
from spacy.lang.es import Spanish
import os
import argparse

def argparser():
    '''
    DESCRIPTION: Parse command line arguments
    '''
    
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-d", "--datapath", required = True, dest = "path", 
                        help = "absolute path to directory with files") 
    
    
    return parser.parse_args().path


def tokenize(text):
    tokenized = []
    nlp = Spanish()
    doc = nlp(text)
    token_list = []
    for token in doc:
        token_list.append(token.text)
        tokenized.append(token_list)
    return token_list

if __name__ == '__main__':
    path = argparser()

    ntokens = 0
    for f in os.listdir(path):
        if f[-3:]!='txt':
            continue
        txt = open(os.path.join(path, f)).read() 
        ntokens = ntokens + len(tokenize(txt))
    print('Files in {} have {} tokens'.format(path, ntokens))
