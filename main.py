import sys
sys.path.append('./lib/')

import ctypes
import os
libdir = os.path.join(os.getcwd(), 'local', 'lib')
libmecab = ctypes.cdll.LoadLibrary(os.path.join(libdir, 'libmecab.so'))

import MeCab

dicdir = os.path.join(os.getcwd(), 'local', 'lib', 'mecab', 'dic', 'ipadic')
rcfile = os.path.join(os.getcwd(), 'local', 'etc', 'mecabrc')
default_tagger = MeCab.Tagger('-d{} -r{}'.format(dicdir, rcfile))

def words(text):
    out_words = []
    default_tagger.parse("")
    node = default_tagger.parseToNode(text)
    while node:
        # word_type = node.feature.split(',')[0]
        out_words.append(node.surface)
        node = node.next
    return out_words

def handle(event, context):
    sentence = "庭には二羽、鶏がいる。"
    results = words(sentence)

    return { 
        'results' : results
    }