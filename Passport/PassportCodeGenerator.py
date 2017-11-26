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
from Dictionaries.Transliterations import Dictionary
from Passport.PassportHashGenerator import PassportHashGenerator
from Passport.PassportHolderName import PassportHolderName


class PassportCodeGenerator(PassportHashGenerator, PassportHolderName, StringCheckers):
    def __init__(self,
                 document_type,
                 country_code,
                 surname,
                 given_names,
                 passport_number,
                 nationality,
                 birth_date,
                 sex,
                 expiry_date,
                 id_number):
        PassportHashGenerator.__init__(self,
                                       passport_number,
                                       birth_date,
                                       expiry_date,
                                       id_number)
        PassportHolderName.__init__(self,
                                    surname,
                                    given_names,
                                    Dictionary.latin_transliteration)

        self.document_type = document_type
        self.country_code = country_code
        self.passport_number = passport_number
        self.nationality = nationality
        self.birth_date = birth_date
        self.sex = sex
        self.expiry_date = expiry_date
        self.id_number = id_number

    @property
    def document_type(self):
        return self._document_type

    @document_type.setter
    def document_type(self, value):
        self._document_type = self._check_field(value, 2, "document type")

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = self._check_field(value, 3, "country code")

    @property
    def passport_number(self):
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value):
        self._passport_number = self._check_field(value, 9, "passport number")

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = self._check_field(value, 3, "nationality code")

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = self._check_sex(value)

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = self._check_field(value, 14, "id number")

    def line1_code_generator(self):
        return self.document_type + \
               self.country_code + \
               self.identifier

    def line2_code_generator(self):
        return self.passport_number + \
               self.passport_number_hash + \
               self.nationality + \
               self.birth_date + \
               self.birth_date_hash + \
               self.sex + \
               self.expiry_date + \
               self.expiry_date_hash + \
               self.id_number + \
               self.id_number_hash + \
               self.final_hash

    def __str__(self):
        return self.line1_code_generator() + "\n" + \
               self.line2_code_generator() + "\n"


xxx = PassportCodeGenerator("P", "UTO", "Eriksson", "Anna Maria", "L898902C3", "UTO", "740812", "F", "120415", "ZE184226B")
print(xxx)