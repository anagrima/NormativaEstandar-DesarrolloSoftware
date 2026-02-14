import json
from UC3MMoney.TransactionManagementException import TransactionManagementException
from UC3MMoney.TransactionRequest import TransactionRequest

class TransactionManager:
    def __init__(self):
        pass

    def ValidateIban( self, iban ):
        # Eliminar espacios y convertir a mayuscula
        iban = iban.strip().upper()
        iban = iban.replace(" ", "").replace("-", "")

        # Verificar que el IBAN tiene 24 caracteres
        if len(iban) != 24:
            return False

        # Verificar que los dos primeros caracteres son "ES"
        if iban[:2] != 'ES':
            return False

        # Mover los 4 primeros caracteres al final
        iban_reordenado = iban[4:] + iban[:4]

        # Convertir las letras a números (A=10, B=11, ..., Z=35)
        iban_numerico = ''
        for caracter in iban_reordenado:
            if caracter.isalpha():
                iban_numerico += str(ord(caracter) - ord('A') + 10)
            else:
                iban_numerico += caracter

        # Calcular el módulo 97 del número resultante
        resto = int(iban_numerico) % 97

        # Si el resto es 1, el IBAN es válido
        return resto == 1


    def ReadProductCodeFromJson( self, fi ):
        try:
            with open(fi, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise TransactionManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise TransactionManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            t_from = data["from"]
            t_to = data["to"]
            to_name = data["receptor_name"]
            req = TransactionRequest(t_from, t_to, to_name)
        except KeyError as e:
            raise TransactionManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateIban(t_from) :
            raise TransactionManagementException("Invalid FROM IBAN")
        if not self.ValidateIban(t_to):
            raise TransactionManagementException("Invalid TO IBAN")
        return req
