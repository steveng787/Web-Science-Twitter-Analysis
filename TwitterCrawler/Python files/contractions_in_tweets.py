# -*- coding: utf-8 -*-

import re
from autocorrect import Speller #pip install autocorrect
check=Speller(lang='en')
from Constructions import contractions
contractions_re = re.compile('(%s)' % '|'.join(contractions.keys()))
def expand_contractions(s, contractions=contractions):
    def replace(match):
        return contractions[match.group(0)]
    return contractions_re.sub(replace, s)
    #replaces any can't etc with the fully expressed version eg. can not. Also have added common shorthand problems to this such as OMG and LOL
    

