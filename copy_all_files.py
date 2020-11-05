#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import os

def copy_all_files(src, dest, _type=None):
    '''
    Copy all files from src to dest
    
    Parameters
    ----------
    src: str. 
        Route to input folder
    dest: str.
        Route to output folder
    _type: str
        File extension to consider. Ex: 'txt'
           
    Returns
    -------
    None
    '''
    
    # create output directory
    if not os.path.exists(dest):
        os.mkdir(dest) 
        
    # Parse input file names
    src_files = os.listdir(src)

    # Select files with given file extension
    if _type != None:
        src_files = list(filter(lambda x: x.split('.')[-1] == _type, src_files))
    
    # Copy files
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
