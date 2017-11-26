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

hf = HashFunctions()
sc = StringCheckers()

class PassportHashGenerator():

    def __init__(self,
                 passport_number_string,
                 birth_date_string,
                 expiry_date_string,
                 id_number_string):
        self.passport_number = passport_number_string
        self.birth_date = birth_date_string
        self.expiry_date = expiry_date_string
        self.id_number = id_number_string

    @property
    def passport_number(self):
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value):
        self._passport_number = value

    @property
    def passport_number_hash(self):
        return hf.hash_string(self.passport_number)

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = sc._check_date(value)

    @property
    def birth_date_hash(self):
        return hf.hash_string(self.birth_date)

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = sc._check_date(value)

    @property
    def expiry_date_hash(self):
        return hf.hash_string(self.expiry_date)

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value

    @property
    def id_number_hash(self):
        return hf.hash_string(self.id_number)

    @property
    def final_hash(self):
        final_string =  self.passport_number + \
                        self.passport_number_hash + \
                        self.birth_date + \
                        self.birth_date_hash + \
                        self.expiry_date + \
                        self.expiry_date_hash + \
                        self.id_number + \
                        self.id_number_hash

        return hf.hash_string(final_string)

    def __str__(self):
        return self.passport_number + " " + \
               self.passport_number_hash + " " + \
               self.birth_date + " " + \
               self.birth_date_hash + " " + \
               self.expiry_date + " " + \
               self.expiry_date_hash + " " + \
               self.id_number + " " + \
               self.id_number_hash + " " + \
               self.final_hash

# aaa = PassportHashGenerator("1234aaa", "790810", "221019", "aaa11222")
# print(aaa)