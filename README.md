Math extension for Python-Markdown
==================================

This extension adds math formulas support to [Python-Markdown].

[Python-Markdown]: https://github.com/waylan/Python-Markdown

Installation
------------

Use `setup.py build` and `setup.py install` to build and install this extension,
respectively.

The extension name is `markdown_mathjax`, so you need to add that name to your
list of Python-Markdown extensions. Check [Python-Markdown documentation] for
details on how to load extensions.

[Python-Markdown documentation]: http://pythonhosted.org/Markdown/extensions/

Usage
-----

To use this extension, you need to include [MathJax] library in HTML files, like:

    <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js"></script>

[MathJax]: http://www.mathjax.org/

Math Delimiters
---------------

For inline math, use `\(...\)`.

For standalone math, use `$$...$$`, `\[...\]` or `\begin...\end`.

The single-dollar delimiter (`$...$`) for inline math is disabled by
default, but can be enabled by passing `single_dollar_delimiter=True`
in the extension configuration.
