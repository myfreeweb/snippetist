#!/usr/bin/env python
import pystache
import yaml

def mksnippet(src):
    src = src.split('\n')
    whitespc = len([True for ch in src[1] if ch == ' '])
    return {'name': src[0],
            'cont': '\n'.join([ln[whitespc-1:] for ln in src[1:]])}

def process(txt):
    txt = txt.split('\n---\n')
    meta = yaml.load(txt[0])
    snippets = map(mksnippet, txt[1].split('\n\n'))
    return snippets