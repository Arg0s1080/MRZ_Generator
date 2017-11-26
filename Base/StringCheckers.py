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
from string import ascii_uppercase
from string import ascii_letters


class StringCheckers:
    @staticmethod
    def _check_date(string):
        try:
            from datetime import datetime
            datetime.strptime(string, "%y%m%d").strftime("%y%m%d")
        except ValueError:
            raise ValueError("String was not recognized as a valid date. It should be 'YYMMDD'", string)
        else:
            return string

    @staticmethod
    def _check_dni_serial_number(string):
        if len(string) == 9:
            lvalue = list(string)
            for char in lvalue[:3]:
                if not char.upper() in ascii_uppercase:
                    lvalue.remove(char)
            for char in lvalue[3:]:
                if not char.isdigit():
                    lvalue.remove(char)
            if len(lvalue) == 9:
                return string.upper()
        raise ValueError("String was not recognized as a valid DNI serial number. "
                         "It should be 3 ascii letters and 6 digits", string)

    @staticmethod
    def _check_nie_serial_number(string):
        if len(string) == 9 and string[0].upper() == "E" and string[1:9].isdigit():
            return string.upper()
        raise ValueError("String was not recognized as a valid NIE serial number. "
                         "It should be 'E' and 8 digits", string)

    @staticmethod
    def _check_nif_number(string, nie=None):
        if int(string) > (99999999 if nie is None else 9999999):
            raise ValueError("Invalid value. The value must be an integer between 1 and 99999999", string)
        return string

    def _parser_full_nif(self, string):
        lvalue = list(string)
        letter = ""

        if not lvalue[0].isdigit():
            raise ValueError("String was not recognized as a valid NIF. "
                             "It should start with a digit", lvalue[0])

        if not lvalue[len(lvalue) - 1].isdigit():
            letter = lvalue.pop(len(string) - 1).upper()
            if letter.upper() not in ascii_uppercase:
                raise ValueError("String was not recognized as a valid NIF. "
                                 "It should end with a digit or a ASCII letter", letter)

        for n in lvalue:
            if not n.isdigit():
                raise ValueError("String was not recognized as a valid NIF. "
                                 "The DNI number should not contain letters inside", n)
        string = self._check_nif_number(int("".join(lvalue)))
        return str(string).zfill(8) + (HashFunctions().hash_dni(string) if letter is "" else letter)

    def _parser_full_nie(self, string):
        lvalue = list(string)
        letter = ""
        nie = lvalue.pop(0).upper()

        if nie not in "XYZ":
            raise ValueError("String was not recognized as a valid NIE. "
                             "It should start with 'X', 'Y' or 'Z'", nie)

        if not lvalue[len(lvalue) - 1].isdigit():
            letter = lvalue.pop(len(lvalue) - 1).upper()
            if letter not in ascii_uppercase:
                raise ValueError("String was not recognized as a valid NIE. "
                                 "It should end with a digit or a ASCII letter", letter)

        for n in lvalue:
            if not n.isdigit():
                raise ValueError("String was not recognized as a valid NIE. "
                                 "The NIE number should not contain letters inside", n)

        string = self._check_nif_number(int("".join(lvalue)), nie)
        string += 0 if nie == "X" else 10000000 if nie == "Y" else 20000000
        return str(string).zfill(8) + (HashFunctions().hash_dni(string) if letter is "" else letter)

    @staticmethod
    def _check_sex(string):
        if len(string) > 1 or string not in "MmFfXx":
            raise ValueError("String was not recognize as a valid genre. "
                             "Sex code should be 'M' or 'F'", string)
        return string.upper()

    @staticmethod
    def _check_field(string, string_length, field_description, exception=""):
        if len(string) > string_length:
            raise ValueError("String was not recognized as a valid " + field_description +
                             ". It should have " + str(string_length) + " characters as maximum", string)
        for c in string:
            if c not in ascii_letters + "0123456789" + exception:
                raise ValueError(field_description + " contains invalid characters", c)

        return string.upper().ljust(string_length, "<")
