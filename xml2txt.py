#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:48:16 2020

@author: antonio
"""
import xml.etree.ElementTree as ET
import os
import argparse


def argparser():
    '''
    DESCRIPTION: Parse command line arguments
    '''
    
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-i", "--input-dir", required = True, dest = "input_dir", 
                        help = "path to input dir with XML files")
    parser.add_argument("-o", "--output-dir", required = True, dest = "output_dir", 
                        help = "path to output dir")
    parser.add_argument("-t", "--xml-tags", required =  True, nargs='+', dest="xml_tags", 
                        help = "List of XML tags from which text will be extracted")
    
    args = parser.parse_args()
    
    return args.input_dir, args.output_dir, args.xml_tags


"""def xml2txt(xml_path, txt_path, xml_tags):
    f = open(txt_path, 'w')
    tree = ET.fromstring(open(xml_path, 'r').read())
    for node in tree.iter(tree.tag):
        for elem in node.iter():
            if (elem.tag in xml_tags) & (elem.text != None):
                #f.write('## ' + elem.tag + '\n')
                f.write(elem.text)
                #f.write('\n\n\n') 
    f.close()"""
    

def xml2txt(xml_path, txt_path, xml_tag):
    f = open(txt_path, 'w')
    tree = ET.fromstring(open(xml_path, 'r').read())
    for node in tree.iter(tree.tag):
        for elem in node.iter():
            if elem.tag != xml_tag:
                continue
            if elem.text == None:
                continue
            if elem.tag == xml_tag == 'EVOL':
                result = ''
                for evol_elem in elem.iter():
                    if evol_elem.tag != 'TEXT':
                        continue
                    if evol_elem.text==None:
                        continue
                    result += evol_elem.text + ' '
                f.write(result)
                continue
            f.write(elem.text)

    f.close()

if __name__ == '__main__':
    
    input_dir, output_dir, xml_tags = argparser()
    
    '''
    input_dir = '/home/antonio/Documents/Projects/covid-19/clinic/Corpus-v10/corpus/CC/xml/'
    output_dir = '/home/antonio/Documents/Projects/covid-19/clinic/Corpus-v10/corpus/CC/txt/'
    xml_tags = ['nota']
    xml_path  = '/home/antonio/Downloads/test-xml2txt/s1/Corpus-v11/corpus/IA/xml/IA.epi.1006710758.xml'
    txt_path = '/home/antonio/Downloads/test-xml2txt/s1/Corpus-v11/corpus/out-test/EVOL_IA.epi.1006710758.xml.txt'
    xml_tags = ['EVOL']
    '''
    
    if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)
    
    for r,d,f in os.walk(input_dir):
        for file in f:
            for tag in xml_tags:
                xml2txt(os.path.join(r,file),
                        os.path.join(output_dir, tag + '_' + file + '.txt'), tag)




