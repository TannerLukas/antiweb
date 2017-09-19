__author__ = "Michael Reithinger, Philipp Rathmanner, Lukas Tanner, Philipp Grandits, and Christian Eitner"
__copyright__ = "Copyright 2017, antiweb team"
__license__ = "GPL"
__version__ = "0.9.1"
__maintainer__ = "antiweb team"
__email__ = "antiweb@freelists.org"

from antiweb_lib.readers.CReader import CReader
from antiweb_lib.readers.CSharpReader import CSharpReader
from antiweb_lib.readers.ClojureReader import ClojureReader
from antiweb_lib.readers.RstReader import RstReader
from antiweb_lib.readers.PythonReader import PythonReader
from antiweb_lib.readers.XmlReader import XmlReader
from antiweb_lib.readers.Language import Language
from fnmatch import fnmatch


#@start(supported_languages doc)

#The following list contains all supported languages:

#@code
supported_languages =[
    Language("C", CReader, ["//"],(["/*","*/"])),
    Language("C++", CReader, ["//"],(["/*","*/"])),
    Language("C#", CSharpReader, ["//"],(["/*","*/"])),
    Language("Python", PythonReader, ["#"],(["'''","'''"],["\"\"\"","\"\"\""])),
    Language("Clojure", ClojureReader, [";"], []),
    Language("reStructuredText", RstReader, [".. "],[]),
    Language("XML", XmlReader, [], (["<!--","-->"]))
]

#sum(list, []) is used to flatten the list as the supported_files of a language are also lists
supported_files = sum([language.supported_files for language in supported_languages], [])
#@edoc

#@(supported_languages doc)

#@start(new_language doc)
'''
New languages can be added by registering a new instance of the Language class
to the supported_languages dictionary as shown in :ref:`Supported Languages <label-supported_languages>`.
A language contains the corresponding pygments lexer, supported_files, reader, single comment characters
and block comment characters (see :ref:`Language <label-language>`).

The comment markers of a language have to be defined in the format:
``[single_comment_tokens]`` and ``[start_block_token, end_block_token]``.
Multiple single and block comment markers can be defined.

If language dependent text processing has to be applied a new Reader class need to be introduced.
A simple Reader example is :py:class:`CReader`, a more advanced Reader is :py:class:`PythonReader`.

Recommended steps when adding a new language:

1) Go to `Available Lexers <http://pygments.org/docs/lexers/>` _ for more information about all available pygments lexers.
2) Implement a new reader class if language specific text processing is needed.
3) Add a new entry for the Language in supported_languages.
'''

#@(new_language doc)

def is_file_supported(file):
    return any(fnmatch(file, supported_file) for supported_file in supported_files)

def get_reader_for_file(file):
    for language in supported_languages:
        for supported_file in language.supported_files:
            if fnmatch(file, supported_file):
                return language.get_reader()