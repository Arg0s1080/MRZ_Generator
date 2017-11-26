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

from Base.Functions import HashFunctions
from Base.StringCheckers import StringCheckers


class DNIHashGenerator(HashFunctions, StringCheckers):
    def __init__(self,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string):
        self.full_dni = full_dni_string
        self.birth_date = birth_date_string
        self.expiration_date = expiration_date_string

    @property
    def full_dni(self):
        return self._full_dni

    @full_dni.setter
    def full_dni(self, value):
        self._full_dni = self._parser_full_nif(value)

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = self._check_date(value)

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = self._check_date(value)

    @property
    def full_dni_hash(self):
        return self.hash_string(self.full_dni)

    @property
    def birth_date_hash(self):
        return self.hash_string(self.birth_date)

    @property
    def expiration_date_hash(self):
        return self.hash_string(self.expiration_date)

    @property
    def final_hash(self):
        return self.hash_string(self.full_dni +
                                self.full_dni_hash +
                                self.birth_date +
                                self.birth_date_hash +
                                self.expiration_date +
                                self.expiration_date_hash)

    def __str__(self):
        return self.full_dni + " " + \
               self.full_dni_hash + " " + \
               self.birth_date + " " + \
               self.birth_date_hash + " " + \
               self.expiration_date + " " + \
               self.expiration_date_hash + " " + \
               self.final_hash

xxx = DNIHashGenerator("12776505", "760504", "760504")
print(xxx)