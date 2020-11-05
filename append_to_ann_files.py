#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import os


def modify_files(new_annots, out_path, with_notes=False, is_sug=True):
    '''
    DESCRIPTION: add annotations to existing files.
    
    Parameters
    ----------
    new_annots: python dict 
        It has new annotations and the file they belong to. 
        {filename: [annotation1, annotatio2, ]}
    out_path: str
        Path to files.
    with_notes: bool
        whether we are writing AnnotationNotes, or not
    is_sug: bool
        Flag. Whether new annotations should appear as suggestions or not
    '''
    files_new_annot = list(new_annots.keys())
    
    for root, dirs, files in os.walk(out_path):
        for filename in files:
            if filename not in files_new_annot:
                continue
            if filename[-3:] != 'txt':
                continue
            filename_ann = filename[0:-3]+ 'ann'
            
            # Get highest mark in ANN
            if os.path.exists(os.path.join(root, filename_ann)) == 0:
                mark = 0
                mode = "w"
            else:
                file_hm = open(os.path.join(root,filename_ann),"r")
                lines = file_hm.readlines()
                if lines:
                    # Get marks
                    marks = list(map(lambda x: int(x.split('\t')[0][1:]),
                                     filter(lambda x: x[0] == 'T', lines)))
                
                    # Get highest mark
                    mark = max(marks)
                else:
                    # Get last mark
                    mark = 0
                mode = "a"
           
            # 2. Write new annotations
            new_annotations = new_annots[filename]
            file = open(os.path.join(root,filename_ann),mode)
            for a in new_annotations:
                mark = mark + 1
                if is_sug == True:
                    label = '_SUG_' +  a[3]
                else:
                    label = a[3]
                file.write('T' + str(mark) + '\t' + label + ' ' + str(a[1]) +
                           ' ' + str(a[2]) + '\t' + a[0] + '\n') 
                if with_notes == False:
                    continue
                file.write('#' + str(mark) + '\t' + 'AnnotatorNotes T' +
                           str(mark) + '\t' + a[4] + '\n')    
