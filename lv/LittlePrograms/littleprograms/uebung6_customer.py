class Customer:
    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addresses = []

    def add_address(self, a: 'Address'):
        self.addresses.append(a)

    def __str__(self):
        return f'{self.name}: {self.phone_number}, {self.email}; {self.addresses}'


class Address:
    def __init__(self, street: str, city: str, postal_code: str, country: str):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country

    def __repr__(self):
        return f'{self.street}, {self.postal_code}, {self.city}, {self.country}'


if __name__ == '__main__':
    c = Customer("Max Kauffroh", "0664 23 943 22", "maxi@kauffroh.at")
    c.add_address(Address("Ökonomiegasse 10", "Graz", "8010", "AT"))
    c.add_address(Address("Ökonomiegasse 33", "Graz", "8010", "AT"))
    print(c)
