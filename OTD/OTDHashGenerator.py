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


class OTDHashGenerator(HashFunctions, StringCheckers):
    def __init__(self,
                 document_number,
                 birth_date,
                 expiry_date,
                 optional_data1="",
                 optional_data2=""):
        self.document_number = document_number
        self.birth_date = birth_date
        self.expiry_date = expiry_date
        self.optional_data1 = optional_data1
        self.optional_data2 = optional_data2

    @property
    def document_number(self):
        return self._document_number

    @document_number.setter
    def document_number(self, value):
        self._document_number = value

    @property
    def document_number_hash(self):
        return self.hash_string(self.document_number)

    @property
    def optional_data1(self):
        return self._optional_data1

    @optional_data1.setter
    def optional_data1(self, value):
        self._optional_data1 = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = self._check_date(value)

    @property
    def birth_date_hash(self):
        return self.hash_string(self.birth_date)

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = self._check_date(value)

    @property
    def expiry_date_hash(self):
        return self.hash_string(self.expiry_date)

    @property
    def optional_data2(self):
        return self._optional_data2

    @optional_data2.setter
    def optional_data2(self, value):
        self._optional_data2 = value

    @property
    def final_hash(self):
        return self.hash_string(self.document_number +
                                self.document_number_hash +
                                self.optional_data1 +
                                self.birth_date +
                                self.birth_date_hash +
                                self.expiry_date +
                                self.expiry_date_hash +
                                self.optional_data2)

    def __str__(self):
        return self.document_number + " " + \
               self.document_number_hash + " " + \
               self.birth_date + " " + \
               self.birth_date_hash + " " + \
               self.expiry_date + " " + \
               self.expiry_date_hash + " " + \
               self.final_hash
