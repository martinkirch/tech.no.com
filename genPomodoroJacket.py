#!/usr/bin/env python
import os
import requests
import string
import sys
 
 
def tex_document(episode, extcolor, intcolor, txtcolor):
    lines = [r'\documentclass[tikz]{standalone}',
             r'\usepackage{tikz}',
             r'\usepackage{fontspec}',
             r'\setmainfont{Inconsolata}',
             r'\begin{document}',
             r'\definecolor{colext}{HTML}{%s}' % extcolor,
             r'\definecolor{colint}{HTML}{%s}' % intcolor,
             r'\definecolor{coltxt}{HTML}{%s}' % txtcolor,
             r'\def\num{%02d}' % episode,
             r'\begin{tikzpicture}',
             r'\node[shape=rectangle, fill=colext, minimum size=2cm] {};',
             r'\node[shape=circle, fill=colint, minimum size=1.5cm]',
             r'{\color{coltxt}\huge\num};',
             r'\end{tikzpicture}',
             r'\end{document}',
             ]
    doc = '\n'.join(lines)
    return doc

 
def palette_named(title_or_code):
    if all(c in string.digits for c in title_or_code):
        url = 'http://www.colourlovers.com/api/palette/{code}'.format(code=title_or_code)
        params={ 'format': 'json', }
    else:
        url = 'http://www.colourlovers.com/api/palettes'
        params={'keywords': title_or_code,
                'keywordExact': 1,
                'format': 'json',
                'numResults': 1
                }
    r = requests.get(url, params=params)
    res = r.json()
    return res[0]['colors']
 
 
def main():
    """
   Usage: make-logo <epname> <palettename> <idx ext>,<idx int>,<idx txt>"
 
   ex: ./make-logo 7 'casual with skirt' 1,2,0
   """
 
    if len(sys.argv) < 3:
        print main.__doc__
        sys.exit(1)
 
    episode = int(sys.argv[1])
    palette_name = sys.argv[2]
    colors = palette_named(palette_name)
    idxs = sys.argv[3].split(',')
    extcolor = colors[int(idxs[0])]
    intcolor = colors[int(idxs[1])]
    txtcolor = colors[int(idxs[2])]
    with open('temp.tex', 'w') as f:
        tex = tex_document(episode, extcolor, intcolor, txtcolor)
        f.write(tex)
    os.system('xelatex -halt-on-error temp')
    os.system('pdftoppm -png -scale-to 256 temp.pdf > temp.png')
 
 
if __name__ == '__main__':
    main()


