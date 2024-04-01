from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError(f'Вказаний номер телефону [{value}] не містить 10 цифр') # !!!


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        try:
            self.phones.append(Phone(phone_number))
        except ValueError as e:
            print(e)

    def find_phone(self, phone_number):
        for el in self.phones:
            if el.value == phone_number:
                return el
        return f'Не знайдено номер телефону [{phone_number}]'

    def remove_phone(self, phone_number):
        self.phones = [el for el in self.phones if el.value != phone_number]

    def edit_phone(self, phone_number, new_phone_number):
        for el in self.phones:
            if el.value == phone_number:
                el.value = new_phone_number
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, record_name):
        return self.data.get(record_name)

    def delete(self, record_name):
        del self.data[record_name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# print(f"Contact name: {john_record.name.value}, phones: {'; '.join(p.value for p in john_record.phones)}")# john_record.__str__()

# Додавання запису John до адресної книги
book.add_record(john_record)
# print(book.data[john_record.name].)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)   

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# john.remove_phone("5555555555")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record) 