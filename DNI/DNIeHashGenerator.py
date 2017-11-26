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


class DNIeHashGenerator(DNIHashGenerator):
    def __init__(self,
                 serial_number_string,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string):
        DNIHashGenerator.__init__(self,
                                  full_dni_string,
                                  birth_date_string,
                                  expiration_date_string)
        self._serial_number = serial_number_string

    def __str__(self):
        return self.serial_number() + " " + \
               self.serial_number_hash() + " " + \
               self.full_dni() + " " + \
               self.birth_date() + " " + \
               self.birth_date_hash() + " " + \
               self.expiration_date() + " " + \
               self.expiration_date_hash() + " " + \
               self.final_hash()

    def serial_number(self):
        return self._check_dni_serial_number(self._serial_number)

    def serial_number_hash(self):
        return self.hash_string(self.serial_number())

    def final_hash(self):
        return self.hash_string(self.serial_number() +
                                self.serial_number_hash() +
                                self.full_dni() +
                                self.birth_date() +
                                self.birth_date_hash() +
                                self.expiration_date() +
                                self.expiration_date_hash())

