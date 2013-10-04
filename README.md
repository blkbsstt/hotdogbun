hotdogbun.py
============

This is a fork of the excellent conference paper splitting script, [hotdogbun](https://github.com/cscorley/hotdogbun),
by [cscorley](https://github.com/cscorley).


Let's split some conference papers in half so we can read them on
smaller devices in continuous scroll mode instead of fumbling around on
the screen like idiots.

All this script does is split each page of a PDF down the middle,
hotdog bun style. **It also tries to determine the bounding box of the
PDF content to create more balanced margins.**

Usage
-----

To split a file './paper.pdf': `python2 hotdogbun.py ./paper.pdf`

That's it. Your split pdf will be located at './paper-split.pdf'

Requirements
------------

Right now, this script uses the [PyPDF2](https://github.com/mstamy2/PyPDF2/) and [pgmagick](https://pypi.python.org/pypi/pgmagick/) python packages. pgmagick is a wrapper around the GraphicsMagick library which uses the Magick++ API through boost.python. Both required packages can be installed through pip.


....Hotdog bun?
---------------
`python2 `<a href="http://en.wikipedia.org/wiki/File:Hotdog_-_Evan_Swigart.jpg"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Hotdog_-_Evan_Swigart.jpg/150px-Hotdog_-_Evan_Swigart.jpg"></a>`.py` <img src="https://raw.github.com/blkbsstt/hotdogbun/master/orig.png" height=300px>
***=======>***
<img src="https://raw.github.com/blkbsstt/hotdogbun/master/split.png" height=300px>


... basically.
