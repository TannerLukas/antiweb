__author__ = "Michael Reithinger, Philipp Rathmanner, Lukas Tanner, Philipp Grandits, and Christian Eitner"
__copyright__ = "Copyright 2017, antiweb team"
__license__ = "GPL"
__version__ = "0.9.1"
__maintainer__ = "antiweb team"
__email__ = "antiweb@freelists.org"

import sys
import pygments.lexers as pm
from pygments.util import ClassNotFound

import logging

logger = logging.getLogger('antiweb')

"""
@start()
.. _label-language:

@include(Language doc)
"""


#@cstart(Language)
class Language(object):
    #@start(Language doc)
    #Language
    #========
    """
    .. py:class:: Language(name, reader, single_comments, block_comments)

       This class represents a supported language of antiweb.
    """

    #@include(Language)
    #@include(Language.__init__ doc)
    #@include(Language.get_reader doc)
    #@(Language doc)


    #@cstart(Language.__init__)
    def __init__(self, name, reader, single_comments, block_comments):
        """
        .. py:method:: __init__(name, reader, single_comments, block_comments)

           The constructor.
           The comment markers of a language have to be defined in the format:
           ``[single_comment_tokens]`` and ``[start_block_token, end_block_token]``.
           Multiple single and block comment markers can be defined.

           :param string name: the name of a pygments lexer.
           :param class reader: the reader class that should be used for the corresponding language.
           :param list single_comments: a list of single comment characters supported by the language (e.g. ['#']).
           :param list<tuple> block_comments: a list of block comment character tuples supported by the language (e.g. ["/*","*/"]).
        """
        try:
            self.lexer = pm.get_lexer_by_name(name)
        except ClassNotFound:
            logger.error("\nError: No lexer for alias: '%s' found", name)
            sys.exit(1)

        self.reader = reader
        self.single_comments = single_comments
        self.block_comments = block_comments

        #the lexer filenames have the format: ['*.cs', '*.cpp', ..]
        self.supported_files = self.lexer.filenames

    #@cstart(Language.get_reader)
    def get_reader(self):
        """
        .. py:method:: get_reader()

           returns a new instance of the :py:attr:`reader` class.
        """
        return self.reader(self.lexer, self.single_comments, self.block_comments)