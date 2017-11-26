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

class Dictionary:
    cyrillic_transliteration = {
        # u"\u0020": "<", u"\u002D": "<",
        u"\u0410": "A", u"\u0430": "a",
        u"\u0411": "B", u"\u0431": "b",
        u"\u0414": "D", u"\u0434": "d",
        u"\u0415": "E", u"\u0435": "e",
        u"\u042D": "E", u"\u044D": "e",
        u"\u0424": "F", u"\u0444": "f",
        u"\u0413": "G", u"\u0433": "g",
        u"\u0418": "I", u"\u0438": "i",
        u"\u0419": "I", u"\u0439": "i",
        u"\u041A": "K", u"\u043A": "k",
        u"\u041B": "L", u"\u043B": "l",
        u"\u041C": "M", u"\u043C": "m",
        u"\u041D": "N", u"\u043D": "n",
        u"\u041E": "O", u"\u043E": "o",
        u"\u041F": "P", u"\u043F": "p",
        u"\u0420": "R", u"\u0440": "r",
        u"\u0421": "S", u"\u0441": "s",
        u"\u0422": "T", u"\u0442": "t",
        u"\u0423": "U", u"\u0443": "u",
        u"\u0412": "V", u"\u0432": "v",
        u"\u042B": "Y", u"\u044B": "y",
        u"\u0417": "Z", u"\u0437": "z",
        u"\u0427": "CH", u"\u0447": "ch",
        u"\u042F": "IA", u"\u044F": "ia",
        u"\u042E": "IU", u"\u044E": "iu",
        u"\u0425": "KH", u"\u0445": "kh",
        u"\u0428": "SH", u"\u0448": "sh",
        u"\u0429": "SHCH", u"\u0449": "shch",
        u"\u0426": "TS", u"\u0446": "ts",
        u"\u0416": "ZH", u"\u0436": "zh"
    }

    latin_transliteration = {
        u"\u0027": "",
        #u"\u0020": "<", u"\u002D": "<",
        u"\u00C1": "A", u"\u00E1": "a",
        u"\u00C0": "A", u"\u00E0": "a",
        u"\u00C2": "A", u"\u00E2": "a",
        u"\u00C4": "AE", u"\u00E4": "ae",
        u"\u00C3": "A", u"\u00E3": "a",
        u"\u0102": "A", u"\u0103": "a",
        u"\u00C5": "AA", u"\u00E5": "aa",
        u"\u0100": "A", u"\u0101": "a",
        u"\u0104": "A", u"\u0105": "a",
        u"\u0106": "C", u"\u0107": "c",
        u"\u0108": "C", u"\u0109": "c",
        u"\u010C": "C", u"\u010D": "c",
        u"\u010A": "C", u"\u010B": "c",
        u"\u00C7": "C", u"\u00E7": "c",
        u"\u0110": "D", u"\u0111": "d",
        u"\u010E": "D", u"\u010F": "d",
        u"\u00C9": "E", u"\u00E9": "e",
        u"\u00C8": "E", u"\u00E8": "e",
        u"\u00CA": "E", u"\u00EA": "e",
        u"\u00CB": "E", u"\u00EB": "e",
        u"\u011A": "E", u"\u011B": "e",
        u"\u0116": "E", u"\u0117": "e",
        u"\u0112": "E", u"\u0113": "e",
        u"\u0118": "E", u"\u0119": "e",
        u"\u0114": "E", u"\u0115": "e",
        u"\u011C": "G", u"\u011D": "g",
        u"\u011E": "G", u"\u011F": "g",
        u"\u0120": "G", u"\u0121": "g",
        u"\u0122": "G", u"\u0123": "g",
        u"\u0126": "H", u"\u0127": "h",
        u"\u0124": "H", u"\u0125": "h",
        u"\u00CD": "I", u"\u00ED": "i",
        u"\u00CC": "I", u"\u00EC": "i",
        u"\u00CE": "I", u"\u00EE": "i",
        u"\u00CF": "I", u"\u00EF": "i",
        u"\u0128": "I", u"\u0129": "i",
        u"\u0130": "I", u"\u0131": "i",
        u"\u012A": "I", u"\u012B": "i",
        u"\u012E": "I", u"\u012F": "i",
        u"\u012C": "I", u"\u012D": "i",
        u"\u0134": "J", u"\u0135": "i",
        u"\u0136": "K", u"\u0137": "i",
        u"\u0141": "L", u"\u0142": "l",
        u"\u0139": "L", u"\u013A": "l",
        u"\u013D": "L", u"\u013E": "l",
        u"\u013B": "L", u"\u013C": "i",
        u"\u013F": "L", u"\u0140": "i",
        u"\u0143": "N", u"\u0144": "n",
        u"\u00D1": "N", u"\u00F1": "n",
        u"\u0147": "N", u"\u0148": "n",
        u"\u0145": "N", u"\u0146": "n",
        u"\u014A": "N", u"\u014B": "n",
        u"\u00D8": "OE", u"\u00F8": "oe",
        u"\u00D3": "O", u"\u00F3": "o",
        u"\u00D2": "O", u"\u00F2": "o",
        u"\u00D4": "O", u"\u00F4": "o",
        u"\u00D6": "OE", u"\u00F6": "oe",
        u"\u00D5": "O", u"\u00F5": "o",
        u"\u0150": "O", u"\u0151": "o",
        u"\u014C": "O", u"\u014D": "o",
        u"\u014E": "O", u"\u014F": "o",
        u"\u0154": "R", u"\u0155": "r",
        u"\u0158": "R", u"\u0159": "r",
        u"\u0156": "R", u"\u0157": "r",
        u"\u015A": "S", u"\u015B": "s",
        u"\u015C": "S", u"\u015D": "s",
        u"\u0160": "S", u"\u0161": "s",
        u"\u015E": "S", u"\u015F": "s",
        u"\u0166": "T", u"\u0167": "t",
        u"\u0164": "T", u"\u0165": "t",
        u"\u0162": "T", u"\u0163": "t",
        u"\u00DA": "U", u"\u00FA": "u",
        u"\u00D9": "U", u"\u00F9": "u",
        u"\u00DB": "U", u"\u00FB": "u",
        u"\u00DC": "UE", u"\u00FC": "ue",
        u"\u0168": "U", u"\u0169": "u",
        u"\u016C": "U", u"\u016D": "u",
        u"\u0170": "U", u"\u0171": "u",
        u"\u016E": "U", u"\u016F": "u",
        u"\u0172": "U", u"\u0173": "u",
        u"\u0174": "W", u"\u0175": "w",
        u"\u00DD": "Y", u"\u00FD": "y",
        u"\u0176": "Y", u"\u0177": "y",
        u"\u0178": "Y", u"\u00FF": "y",
        u"\u0179": "Z", u"\u017A": "z",
        u"\u017D": "Z", u"\u017E": "z",
        u"\u017B": "Z", u"\u017C": "u",
        u"\u00DE": "TH", u"\u00FE": "th",
        u"\u00C6": "AE", u"\u00E6": "ae",
        u"\u0132": "IJ", u"\u0133": "ij",
        u"\u0152": "OE", u"\u0153": "oe",
        u"\u00DF": "SS", u"\u1E9E": "ss"
    }


def transliterate(string, dictionary):
    final_string = ""
    for char in string:
        final_string += dictionary[char] if char in dictionary else char
    return final_string.upper()



