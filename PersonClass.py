class Person:
    def __init__(self, name, address, telephone_number):
        self.__fullName = name
        self.__address = address
        self.__phone = telephone_number

    def get_fullName(self):
        return self.__fullName

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print(self.get_fullName(), self.get_address(), self.get_phone())


class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number, Mailing_list):
        Person.__init__(self, name, address, telephone_number)

        self.__custNumb = customer_number
        self.__mailingList = Mailing_list

    def get_custNumb(self):
        return self.__custNumb

    def get_mail(self):
        return self.__mailingList

    def print_person(self):
        Person.print_person(self)
        print(
            self.get_custNumb(),
            self.get_mail(),
        )
