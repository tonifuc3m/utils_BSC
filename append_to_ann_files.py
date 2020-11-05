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
    new_annots: pandas DataFrame
        It has the new annotations and the file they belong to. 
        Required column names: ['filename', 'offset', 'label', 'span']
    out_path: str
        Path to files.
    with_notes: bool
        whether we are writing AnnotationNotes, or not
    is_sug: bool
        Flag. Whether new annotations should appear as suggestions or not
    '''
    files_new_annot = set(new_annots.filename.to_list())
    
    for root, dirs, files in os.walk(out_path):
        for filename in files:
            if filename not in files_new_annot:
                continue
            if filename[-3:] != 'ann':
                continue
            
            # Get highest mark in ANN
            if os.path.exists(os.path.join(root, filename)) == 0:
                mark = 0
                mode = "w"
            else:
                file_hm = open(os.path.join(root,filename),"r")
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
            new_annotations = new_annots.loc[new_annots['filename'] == filename,:]
            file = open(os.path.join(root,filename),mode)
            for idx, a in new_annotations.iterrows():
                mark = mark + 1
                if is_sug == True:
                    label = '_SUG_' +  a['label']
                else:
                    label = a['label']
                file.write('T' + str(mark) + '\t' + label + ' ' + a['offset'] +
                           '\t' + a['span'] + '\n') 
                if with_notes == False:
                    continue
                file.write('#' + str(mark) + '\t' + 'AnnotatorNotes T' +
                           str(mark) + '\t' + a['code'] + '\n')    
