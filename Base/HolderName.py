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

from Base.StringCheckers import StringCheckers
from Dictionaries.Transliterations import *


class HolderName(StringCheckers, Dictionary):
    def __init__(self, surname, given_names, transliteration=Dictionary.latin_transliteration):
        self.transliteration = transliteration
        self.surname = surname
        self.given_names = given_names

    def _identifier_parser(self, string, sep="<"):
        identifier = string.replace(u"\u002D", u"\u0020").split(u"\u0020")
        for i in range(len(identifier)):
            identifier[i] = transliterate(identifier[i], self.transliteration)
        return sep.join(identifier)

    @property
    def transliteration(self):
        return self._transliteration

    @transliteration.setter
    def transliteration(self, value):
        self._transliteration = value

    @property
    def surname(self):
        return self._surnames

    @surname.setter
    def surname(self, value):
        self._surnames = self._identifier_parser(value)

    @property
    def given_names(self):
        return self._given_names

    @given_names.setter
    def given_names(self, value):
        self._given_names = self._identifier_parser(value)

    def __str__(self):
        return self.surname + "<<" + self.given_names
