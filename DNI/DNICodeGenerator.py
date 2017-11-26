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

from DNI.DNIHashGenerator import DNIHashGenerator


class DNICodeGenerator(DNIHashGenerator):
    def __init__(self,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string,
                 sex_string="M",
                 nationality_string="ESP",
                 document_type_string="ID",
                 country_code_string="ESP"):
        DNIHashGenerator.__init__(self,
                                  full_dni_string,
                                  birth_date_string,
                                  expiration_date_string)
        self.sex = sex_string.upper()
        self.nationality = nationality_string.upper()
        self.country_code = country_code_string.upper()
        self.document_type = document_type_string.upper()

    def __str__(self):
        return self.line1_code_generator() + \
               "\n" + \
               self.line2_code_generator()

    def line1_code_generator(self):
        return (self.document_type +
                self.country_code +
                self.full_dni +
                self.full_dni_hash).ljust(30, "<")

    def line2_code_generator(self):
        return (self.birth_date +
                self.birth_date_hash +
                self.sex +
                self.expiration_date +
                self.expiration_date_hash +
                self.nationality).ljust(29, "<") + \
                self.final_hash
