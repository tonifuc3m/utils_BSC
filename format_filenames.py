#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:11:47 2019

@author: antonio
"""

import os
############# Make a copy of entire directory so we do not lose the originals #################    


def format_filenames(datapath, copy=False):
    
    if copy == True:
        ############# Make a copy of entire directory so we do not lose the originals #################
    
        # First, remove spaces (DONE through command line)
        
        # Then, remove weird characters
        for root, dirs, files in os.walk(datapath):
            for filename in files:
                if filename[-3:] == 'pdf': # get only txt files
                    
                    # Remove internal dots
                    filename_no_dots = filename.replace('.', '')
                    filename_list = list(filename_no_dots)
                    filename_list[-3:] = list('.pdf')
                    filename_one_dot = "".join(filename_list)
                    
                    # Remove internal commas and accents
                    old_symbols = [',', 'á', 'é', 'í', 'ó', 'ú']
                    new_symbols = ['', 'a', 'e', 'i', 'o', 'u']
                    filename_new_symbols = filename_one_dot
                    for old, new in zip(old_symbols, new_symbols):
                        filename_new_symbols = filename_new_symbols.replace(',', '')
                        
                    # Rename file
                    os.rename(os.path.join(root,filename), os.path.join(root, filename_new_symbols))
                    
        else:
            print('Make a copy of entire directory so we do not lose the originals,then, change copy parameter to True')              
if __name__ == '__main__':
    ############# Make a copy of entire directory so we do not lose the originals #################    

    datapath = '/home/antonio/Downloads/ecimed_splitted'
    format_filenames(datapath, copy=False)