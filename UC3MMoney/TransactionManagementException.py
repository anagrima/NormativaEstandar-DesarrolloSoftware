class TransactionManagementException(Exception):
    def __init__(self, message):
        self.__message = message
        super().__init__(self.Message)

    @property
    def Message(self):
        return self.__message

    @Message.setter
    def Message(self,value):
        self.__message = value
