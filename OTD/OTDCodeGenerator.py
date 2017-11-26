from Base.StringCheckers import StringCheckers
from Dictionaries.Transliterations import Dictionary
from OTD.OTDHashGenerator import OTDHashGenerator
from OTD.OTDHolderName import OTDHolderName


class OTDCodeGenerator(OTDHolderName, OTDHashGenerator, StringCheckers):
    def __init__(self,
                 document_type,
                 country_code,
                 document_number,
                 birth_date,
                 sex,
                 expiry_date,
                 nationality,
                 surname,
                 given_names,
                 transliteration=Dictionary.latin_transliteration,
                 optional_data1="",
                 optional_data2=""):
        OTDHashGenerator.__init__(self, document_number, birth_date, expiry_date, optional_data1, optional_data2)
        OTDHolderName.__init__(self, surname, given_names, transliteration)

        self.document_type = document_type
        self.country_code = country_code
        self.document_number = document_number
        self.optional_data1 = optional_data1
        self.birth_date = birth_date
        self.sex = sex
        self.expiry_date = expiry_date
        self.nationality = nationality
        self.optional_data2 = optional_data2

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
    def document_number(self):
        return self._document_number

    @document_number.setter
    def document_number(self, value):
        self._document_number = self._check_field(value, 9, "passport number")

    @property
    def optional_data1(self):
        return self._optional_data1

    @optional_data1.setter
    def optional_data1(self, value):
        self._optional_data1 = self._check_field(value, 15, "optional data 1")

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = self._check_sex(value)

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = self._check_field(value, 3, "nationality code")

    @property
    def optional_data2(self):
        return self._optional_data2

    @optional_data2.setter
    def optional_data2(self, value):
        self._optional_data2 = self._check_field(value, 11, "optional data 2")

    def line1_code_generator(self):
        return(self.document_type +
               self.country_code +
               self.document_number +
               self.document_number_hash +
               self.optional_data1)

    def line2_code_generator(self):
        return(self.birth_date +
               self.birth_date_hash +
               self.sex +
               self.expiry_date +
               self.expiry_date_hash +
               self.nationality +
               self.optional_data2 +
               self.final_hash)

    def __str__(self):
        return(self.line1_code_generator() +
               "\n" +
               self.line2_code_generator() +
               "\n" +
               self.identifier)

xxx = OTDCodeGenerator("ID", "ESP", "12776505M", "760504", "M", "201116", "esp", "ricón gómez", "iván mANUEL")
xxx = OTDCodeGenerator("ID", "ESP", "ALM196431", "760504", "M", "201116", "ESP", "rinCÓN GOMEZ", "IVÁN MANUEL", Dictionary.latin_transliteration, "12776505M")
print(xxx)
