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

from DNI.DNIeHashGenerator import DNIeHashGenerator


class NIEHashGenerator(DNIeHashGenerator):
    def __init__(self,
                 serial_number_string,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string):
        DNIeHashGenerator.__init__(self,
                                   serial_number_string,
                                   full_dni_string,
                                   birth_date_string,
                                   expiration_date_string)
        self._serial_number = serial_number_string
        self._full_nie = full_dni_string

    def serial_number(self):
        return self._check_nie_serial_number(self._serial_number)

    def full_dni(self):
        return self._parser_full_nie(self._full_nie)
