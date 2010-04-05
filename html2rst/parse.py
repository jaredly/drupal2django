#!/usr/bin/env python2.6
from BeautifulSoup import BeautifulSoup, Tag, NavigableString
import re

def convert_html(text, **args):
    p = Parser(text, **args)
    p.parse()
    return p

class Parser:
    def __init__(self, text, media_root=None, drupal_root=None, media_url='/media/'):
        self.text = text
        self.media_root = media_root
        if self.media_root:
            self.image_root = os.path.join(media_root, 'images')
        else:
            self.image_root = None

        if self.media_root and not os.path.exists(self.image_root):
            os.mkdir(self.image_root)
        self.drupal_root = drupal_root
        self.media_url = media_url
        self.skipped = False
        self.images = []

    def parse(self):
        soup = BeautifulSoup(self.text)
        self.rest = self.parsetag(soup)

    def parsetag(self, tag):
        text = ''
        for item in tag:
            if isinstance(item, NavigableString):
                text += unicode(item)
            else:
                stext = parsetag(item)
                text += stext
        ## paragraph
        if tag.name in ('div','p'):
            if '\n' not in text:
                return '\n\n' + linelength(text,79) + '\n\n'
            else:
                return '\n\n' + text + '\n\n'
        ## preformatted
        elif tag.name in ('pre', 'code'):
            return u'\n\n.. code-block:: python\n\n' + u'    ' + text.replace(u'\n',u'\n    ') + u'\n\n'
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
            return u'\n\n' + quote[1:] + '\n\n'
        ## links
        elif tag.name == 'a':
            if '\n' in text:
                return text, True
            return u'`%s <%s>`_' % (text, tag['href'])
        ## line breaks
        elif tag.name == 'br':
            return u'\n\n', skipped
        ## bold text
        elif tag.name in ('strong','b'):
            return u'**%s**' % text
        ## italics
        elif tag.name in ('em','i'):
            return u'*%s*' % text
        ## headers
        elif tag.name in ('h1','h2','h3','h4'):
            styles = {'h1':'=','h2':'-','h3':'~','h4':'#'}
            return '\n\n' + text.replace('\n',' ').strip() + '\n' + styles[tag.name] * len(text) + '\n\n'
        ## images
        elif tag.name == 'img':
            src = self.move_file(tag['src'])
            width = tag.get('width','')
            height = tag.get('height','')
            alt = tag.get('alt','')
            text = '\n\n.. image:: %s\n' % src
            if width:text += '   :width: %s\n' % width
            if height:text += '   :height: %s\n' % height
            if alt:text += '   :alt: %s\n' % alt
            return text + '\n'
        elif tag.name in ('object', 'embed', 'style', 'script', 'textarea'):
            self.skipped = True
            return ''
        ## main document
        elif tag.name == '[document]':
            text = re.sub('\n\s+\n', '\n\n', text)
            text = text.replace('&nbsp;',' ').replace('&lt','<').replace('&gt;','>').replace('&amp;','&')
            return text
        else:
            print 'Unhandled tag:',tag.name
            self.skipped = True
        return text
    
    def move_file(self, src):
        if self.image_root is None:
            return src
        base = os.path.basename(src)
        if os.path.exists(os.path.join(self.image_root, base)):
            print 'skipping',src
        else:
            open(os.path.join(self.image_root, base), 'wb').write(open(os.path.join(self.drupal_root, src),'rb').read())
        return os.path.join(self.media_url, 'images', base)

def linelength(text, width):
    lines = ['']
    for word in text.split(' '):
        if len(lines[-1])+len(word) > width:
            lines.append('')
        lines[-1] += word + ' '
    return '\n'.join(lines)

if __name__=='__main__':
    rest = convert_html(open('../test2.html').read())


# vim: et sw=4 sts=4
