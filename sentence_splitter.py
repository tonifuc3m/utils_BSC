from sentence_splitter import SentenceSplitter # recommended by jordi
import argparse
import os

def argparser():
    '''
    DESCRIPTION: Parse command line arguments
    '''
    
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-d", "--datapath", required = True, dest = "path", 
                        help = "absolute path to directory with files") 
    
    
    return parser.parse_args().path


def split_to_sentences(text, target_lang='es'):
    '''
    DESCRIPTION: Split text into sentences.

    Parameters
    ----------
    text : string
        String with entire document.

    Returns
    -------
    sentences: list of str
        List with sentences of document

    '''  
    splitter = SentenceSplitter(language=target_lang)
    return splitter.split(text) 


if __name__ == '__main__':
    path = argparser()

    nsent = 0
    for f in os.listdir(path):
        if f[-3:]!='txt':
            continue
        txt = open(os.path.join(path, f)).read() 
        nsent = nsent + len(split_to_sentences(txt))
    print('Files in {} have {} sent'.format(path, nsent))

