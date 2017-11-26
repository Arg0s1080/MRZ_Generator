#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from DNI.DNIeCodeGenerator import DNIeCodeGenerator
from DNI.DNICodeGenerator import DNICodeGenerator
from DNI.NIECodeGenerator import NIECodeGenerator
from datetime import datetime

# Colours
W = "\033[0m"
R = "\033[31m"
G = "\033[32m"
O = "\033[33m"
B = "\033[34m"


def date_format(input_string):
    return datetime.strptime(input_string, "%d/%m/%Y").strftime("%y%m%d")


try:
    print("=".ljust(47, "="))
    print("EJEMPLO DE UTILIZACIÓN DNI(e) CODE GENERATOR")
    print("=".ljust(47, "="))

    serial_number = input("Número de serie del documento ".ljust(47, "."))
    full_dni = input("Número DNI con o sin letra (Ej. 12345678) ".ljust(47, "."))
    birth_date = date_format(input("Fecha de nacimiento (Ej. 31/12/1980) ".ljust(47, ".")))
    expiration_date = date_format(input("Fecha de caducidad documento (Ej. 20/08/2020) ".ljust(47, ".")))

    print("\nElija qué tipo de documento imprimir:")
    print("a) DNIe")
    print("b) DNI Antiguo")
    print("c) NIE")
    answer = input(">")

    if answer == "a":
        print("=".ljust(47, "="))
        print("CÓDIDO DNIe:")
        print("=".ljust(47, "="))
        print(DNIeCodeGenerator(serial_number, full_dni, birth_date, expiration_date))
    elif answer == "b":
        print("=".ljust(47, "="))
        print("CÓDIGO DNI VIEJO:")
        print("=".ljust(47, "="))
        print(DNICodeGenerator(full_dni, birth_date, expiration_date))
    elif answer == "c":
        print("=".ljust(47, "="))
        print("CÓDIDO NIE:")
        print("=".ljust(47, "="))
        sex = input("Género (Ej. M)".ljust(47, "."))
        nationality = input("Código nacionalidad (Ej USA)".ljust(47, "."))
        print("=".ljust(47, "="))
        print(NIECodeGenerator(serial_number, full_dni, birth_date, expiration_date, sex, nationality))

except ValueError as error:
    print("Error:", error.args[0])