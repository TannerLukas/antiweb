.. _label-language:

Language
========
.. py:class:: Language(name, reader, single_comments, block_comments)

   This class represents a supported language of antiweb.


::

    class Language(object):
    
    
        <<Language.__init__>>
        <<Language.get_reader>>

.. py:method:: __init__(name, reader, single_comments, block_comments)

   The constructor.
   The comment markers of a language have to be defined in the format:
   ``[single_comment_tokens]`` and ``[start_block_token, end_block_token]``.
   Multiple single and block comment markers can be defined.

   :param string name: the name of a pygments lexer.
   :param class reader: the reader class that should be used for the corresponding language.
   :param list single_comments: a list of single comment characters supported by the language (e.g. ['#']).
   :param list<tuple> block_comments: a list of block comment character tuples supported by the language (e.g. ["/*","*/"]).
   
   ::
   
       def __init__(self, name, reader, single_comments, block_comments):
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
       
   
.. py:method:: get_reader()

   returns a new instance of the :py:attr:`reader` class.
   
   ::
   
       def get_reader(self):
           return self.reader(self.lexer, self.single_comments, self.block_comments)
   

