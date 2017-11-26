#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# DNI_Code_Generator is licensed under the:
# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned
# on making available complete source code of licensed works
# and modifications, which include larger works using a licensed
# work, under the same license. Copyright and license notices
# must be preserved. Contributors provide an express grant of
# patent rights.
#
# For more information on this, and how to apply and follow the
# GNU GPL, see http://www.gnu.org/licenses
#
# Iván Rincón 2017

from Base.HolderName import HolderName
from Dictionaries.Transliterations import *


class PassportHolderName(HolderName):
    def __init__(self, surname, given_names, transliteration=Dictionary.latin_transliteration):
        HolderName.__init__(self, surname, given_names, transliteration)

    @property
    def identifier(self):
        return self._check_field(self.surname + "<<" + self.given_names, 39, "full name", "<")
