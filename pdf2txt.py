#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:26:57 2019

@author: antonio
"""

import os
import re
from tika import parser

def copy_dir_structure(path, input_path_old_files, output_path_new_files):
    for dirpath, dirnames, filenames in os.walk(path + input_path_old_files):
        structure = os.path.join(path + output_path_new_files, 
                                 dirpath[len(path + input_path_old_files):])
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            print("Folder does already exist!")
            

def pdf2txt(datapath):
    for root, dirs, files in os.walk(datapath):
        for filename in files:
            if filename[-3:] == 'pdf': # get only pdf files
                root_new = root.replace(re.search(pdf_path, root).group(), txt_path)
                root_sp = root.split('/')
                root_sp[4] = 'ecimed_splitted_txt'
                root_new = '/'.join(root_sp)
                filename_new = filename + '.txt'
                
                raw = parser.from_file(os.path.join(root, filename))
                try:
                    content = raw['content']
                    
                    safe_text = content.encode('utf-8', errors='ignore')                
                    
                    text_file = open(os.path.join(root_new, filename_new), "w")
                    text_file.write(safe_text)
                    text_file.close()
                except:
                    print('Empty parsed file {}'.format(os.path.join(root, filename)))
            
if __name__ == '__main__':
    path = '/home/antonio/Downloads/'
    pdf_path = 'ecimed_splitted/'
    txt_path = pdf_path[0:-1] + '_txt/'
    copy_dir_structure(path, pdf_path, txt_path)
    pdf2txt(os.path.join(path, pdf_path), pdf_path, txt_path)