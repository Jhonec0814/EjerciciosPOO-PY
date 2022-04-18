from mailbox import NoSuchMailboxError


class Cliente:

    def __init__(self,name,lastName,id,accountNumber):

        self.name = name
        self.lastName = lastName
        self.id = id
        self.accountNumber = accountNumber