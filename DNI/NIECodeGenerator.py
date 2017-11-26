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

from DNI.DNICodeGenerator import DNICodeGenerator
from DNI.NIEHashGenerator import NIEHashGenerator


class NIECodeGenerator(DNICodeGenerator, NIEHashGenerator):
    def __init__(self,
                 serial_number_string,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string,
                 sex_string="M",
                 nationality_string="ESP",
                 country_code_string="ESP",
                 document_type_string="IX"):
        NIEHashGenerator.__init__(self,
                                  serial_number_string,
                                  full_dni_string,
                                  birth_date_string,
                                  expiration_date_string)
        DNICodeGenerator.__init__(self,
                                  full_dni_string,
                                  birth_date_string,
                                  expiration_date_string,
                                  sex_string,
                                  nationality_string,
                                  country_code_string,
                                  document_type_string)

    def line1_code_generator(self):
        return (self.document_type +
                self.country_code +
                self.serial_number().ljust(10, "<") +
                self.serial_number_hash() +
                self.full_dni()).ljust(30, "<")
