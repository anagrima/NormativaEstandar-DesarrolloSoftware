import json
from datetime import datetime, UTC


class TransactionRequest:
    def __init__(self, iban_from, iban_to, receptor_name):
        self.__receptor_name = receptor_name
        self.__iban_from = iban_from
        self.__iban_to = iban_to
        justnow = datetime.now(UTC)
        self.__time_stamp = justnow.timestamp()

    def __str__(self):
        return "TransactionRequest:" + json.dumps(self.__dict__)

    @property
    def ReceptorName(self):
        return self.__receptor_name
    @ReceptorName.setter
    def ReceptorName(self, value):
        self.__receptor_name = value

    @property
    def IbanFrom(self):
        return self.__iban_from
    @IbanFrom.setter
    def IbanFrom(self, value):
        self.__iban_from = value

    @property
    def IbanTo(self):
        return self.__iban_to
    @IbanTo.setter
    def IbanTo(self, value):
        self.__iban_to = value

    @property
    def TimeStamp(self):
        return self.__time_stamp
