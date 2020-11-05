#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:43:15 2020

@author: antonio
"""

import os
import pandas as pd


def tsv2ann(df, out_path, with_notes = False):
    '''
    Copy all files from src to dest
    
    Parameters
    ----------
    df: pandas DataFrame
        contain annotation information. 
        Required columns: ['filename', 'offset', 'label', 'span']
        'offset' column must have initial and final positions separated by a blankspace
    out_path: str.
        Route to output folder
    with_notes: bool
        Flag. Whether to include AnnotatorNotes in Brat or not
           
    Returns
    -------
    None
    '''

    # create output directory
    if not os.path.exists(out_path):
        os.mkdir(out_path) 
        
    files = set(df['filename'].to_list())
    
    for _file in files:
        df_this = df[df['filename'] == _file]
        mark = 0
        f = open(os.path.join(out_path, _file), 'w')
        
        for index, row in df_this.iterrows():
            mark = mark + 1
            pos = row['offset']
            label = row['label']
            span = row['span']
            f.write('T' + str(mark) + '\t' + label + ' ' + str(pos) + '\t' + 
                    span + '\n')
            if with_notes==False:
                continue
            code = row['code']
            f.write('#' + str(mark) + '\tAnnotatorNotes T' + str(mark) + '\t' + 
                    str(code) + '\n')
                