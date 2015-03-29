# -*- coding: utf-8 -*-

'''
Math extension for Python-Markdown
==================================

Adds support for displaying math formulas using
[MathJax](http://www.mathjax.org/).

Authors:
    2015, Dmitry Shachnev <mitya57@gmail.com>,
    2015, Sam Toyer <sam@qxcv.net>
'''

import markdown


class MathExtension(markdown.extensions.Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'enable_dollar_delimiter': [
                False, 'Enable single-dollar delimiter'
            ],
        }
        super(MathExtension, self).__init__(*args, **kwargs)

    inlinemathpatterns = (
        #  $...$
        markdown.inlinepatterns.Pattern(r'(?<!\\|\$)(\$)([^\$]+)(\$)'),
        # \(...\)
        markdown.inlinepatterns.Pattern(r'(?<!\\)(\\\()(.+?)(\\\))')
    )

    mathpatterns = (
        # $$...$$
        markdown.inlinepatterns.Pattern(r'(?<!\\)(\$\$)([^\$]+)(\$\$)'),
        # \[...\]
        markdown.inlinepatterns.Pattern(r'(?<!\\)(\\\[)(.+?)(\\\])'),
        markdown.inlinepatterns.Pattern(
            r'(?<!\\)(\\begin{[a-z]+\*?})(.+)(\\end{[a-z]+\*?})'
        )
    )

    def handle_match_inline(self, m):
        node = markdown.util.etree.Element('span')
        node.text = markdown.util.AtomicString(r'\(' + m.group(3) + r'\)')
        return node

    def handle_match(self, m):
        node = markdown.util.etree.Element('div')
        node.text = markdown.util.AtomicString(m.group(3))
        if '\\begin' in m.group(2):
            node.text = markdown.util.AtomicString(
                m.group(2) + m.group(3) + m.group(4)
            )
        node.text = markdown.util.AtomicString(r'\[{}\]'.format(node.text))
        return node

    def extendMarkdown(self, md, md_globals):
        configs = self.getConfigs()
        inlinemathpatterns = self.inlinemathpatterns
        if not configs['enable_dollar_delimiter']:
            inlinemathpatterns = self.inlinemathpatterns[1:]
        for i, pattern in enumerate(inlinemathpatterns):
            pattern.handleMatch = self.handle_match_inline
            md.inlinePatterns.add('math-inline-%d' % i, pattern, '<escape')
        for i, pattern in enumerate(self.mathpatterns):
            pattern.handleMatch = self.handle_match
            md.inlinePatterns.add('math-%d' % i, pattern, '<escape')


def makeExtension(*args, **kwargs):
    return MathExtension(*args, **kwargs)
