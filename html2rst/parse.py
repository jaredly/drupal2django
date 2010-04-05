#!/usr/bin/env python2.6
from BeautifulSoup import BeautifulSoup, Tag, NavigableString
import re

def convert_html(text):
    soup = BeautifulSoup(text)
    return parsetag(soup)

def parsetag(tag):
    text = ''
    skipped = False
    for item in tag:
        if isinstance(item, NavigableString):
            text += unicode(item)
        else:
            stext, sk = parsetag(item)
            if sk:skipped = sk
            text += stext
    ## paragraph
    if tag.name in ('div','p'):
        if '\n' not in text:
            return '\n\n' + linelength(text,79) + '\n\n', skipped
        else:
            return '\n\n' + text + '\n\n', skipped
    ## preformatted
    elif tag.name in ('pre', 'code'):
        return u'\n\n.. code-block:: python\n\n' + u'    ' + text.replace(u'\n',u'\n    ') + u'\n\n', skipped
    ## blockquote
    elif tag.name == 'blockquote':
        quote = ''
        # remove headers
        for line in text.split('\n'):
            l = line.strip()
            if l and l == l[0]*len(l):
                print 'removing header from blockquote'
                continue
            quote += '\n    ' + line
        return u'\n\n' + quote[1:] + '\n\n', skipped
    ## links
    elif tag.name == 'a':
        if '\n' in text:
            return text, True
        return u'`%s <%s>`_' % (text, tag['href']), skipped
    ## line breaks
    elif tag.name == 'br':
        return u'\n\n', skipped
    ## bold text
    elif tag.name in ('strong','b'):
        return u'**%s**' % text, skipped
    ## italics
    elif tag.name in ('em','i'):
        return u'*%s*' % text, skipped
    ## headers
    elif tag.name in ('h1','h2','h3','h4'):
        styles = {'h1':'=','h2':'-','h3':'~','h4':'#'}
        return '\n\n' + text.replace('\n',' ').strip() + '\n' + styles[tag.name] * len(text) + '\n\n', skipped
    ## images
    elif tag.name == 'img':
        src = tag['src']
        width = tag.get('width','')
        height = tag.get('height','')
        alt = tag.get('alt','')
        text = '\n\n.. image:: %s\n' % src
        if width:text += '   :width: %s\n' % width
        if height:text += '   :height: %s\n' % height
        if alt:text += '   :alt: %s\n' % alt
        return text + '\n', skipped
    elif tag.name in ('object', 'embed', 'style', 'script', 'textarea'):
        return '', True
    ## main document
    elif tag.name == '[document]':
        text = re.sub('\n\s+\n', '\n\n', text)
        text = text.replace('&nbsp;',' ').replace('&lt','<').replace('&gt;','>').replace('&amp;','&')
        return text, skipped
    else:
        print 'Unhandled tag:',tag.name
        skipped = True

    return text, skipped

def linelength(text, width):
    lines = ['']
    for word in text.split(' '):
        if len(lines[-1])+len(word) > width:
            lines.append('')
        lines[-1] += word + ' '
    return '\n'.join(lines)


#print soup.prettify()

if __name__=='__main__':
    text, sk = convert_html(open('../test2.html').read())


# vim: et sw=4 sts=4
