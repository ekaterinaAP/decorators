from param_decor_logger import param_decor_logger


class Contact:

    def __init__(self, first_name, last_name, phone, favorite=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.favorite = favorite
        self.add_information = kwargs

    def __str__(self):
        if self.favorite is False:
            favorite_ru = 'Нет'
        else:
            favorite_ru = 'Да'
        return (
            f'Имя: {self.first_name}\n'
            f'Фамилия: {self.last_name}\n'
            f'Номер телефона: {self.phone}\n'
            f'В избранных: {favorite_ru}\n'
            f'Дополнительная информация: {self.add_information}'
        )


class PhoneBook:

    def __init__(self, name_book):
        self.name = name_book
        self.contacts_list = []

    def get_contacts(self):
        for contact in self.contacts_list:
            print(contact)

    @param_decor_logger('log.txt')
    def add_contact(self, contact):
        self.contacts_list.append(contact)

    def del_contact(self, phone):
        for contact in self.contacts_list:
            if contact.phone == phone:
                self.contacts_list.remove(contact)

    def get_favorite(self):
        for contact in self.contacts_list:
            if contact.favorite:
                print(contact)

    def get_contact(self, first_name, last_name):
        for contact in self.contacts_list:
            if (contact.first_name == first_name) and (contact.last_name == last_name):
                print(contact)


if __name__ == '__main__':
    phone_book = PhoneBook('abc')

    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    phone_book.add_contact(jhon)

    Anna = Contact('Anna', 'Anna', '+79034567891')

    print()
    phone_book.add_contact(Anna)
    phone_book.get_contacts()

    print()
    phone_book.del_contact('+79034567891')
    phone_book.get_contacts()

    print()
    phone_book.get_favorite()

    print()
    phone_book.get_contacts()

    print()
    jhonny = Contact('jhon', 'ghjk', '+77894561212')
    phone_book.add_contact(jhonny)
    phone_book.get_contact('jhon', 'ghjk')

