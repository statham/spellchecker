spellchecker
============

coding challenge: http://www.twitch.tv/problems/spellcheck

##Usage

Run script with
'''
python -c "from spellchecker import *; print spellcheck()"
'''

##Runtime
The runtime for this spellchecker can be found to be O(m), where m is the size of the string being checked. This can be achieved by use of a trie to represent the dictionary of words. The algorithm first finds a finite number of possible mutations of the input word by taking into account possible misuse of case, repeated letters, and incorrect vowels. The possible mutations which are all less than or equal to the size of the input word, m, are then checked for in the trie, and either the first correct word is returned, or no suggestion is returned.
