"""Cvičení 5

Napiš třídu, která bude představovat sklad.
Kapacita skladu (desetinné hodnoty reprezentující kubické metry) je definována konstruktorem.

Vytvoř třídu, která bude představovat produkt. Objem produktu je určen konstruktorem.

Sklad bude mít metodu "add", která vezme objekt Product jako svůj argument
a vrátí jeho zbývající volný prostor nebo -1 pokud do něj nejde přidat předmět z nedostatku prostoru.

Použij fixture na přípravu množiny produktů, které se umísťují do skladu každý měsíc a vytvoř testy,
které budou kontrolovat jestli sklad správně přidává produkty.
Přesnost na dvě desetinná místa."""


class Product:
    __name = None
    __volume = None

    def __init__(self, name: str, volume: float):
        self.name = name
        self.volume = volume

    def __repr__(self):
        return f"Product(name={self.name}, volume={self.volume})"

    def __str__(self):
        return f"Product '{self.name}' with volume '{self.volume}'"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_: str):
        self.__name = name_

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume_: float):
        if not isinstance(volume_, (int, float)):  # testujeme, zda je zadané číslo
            raise TypeError
        if volume_ < 0:  # testujeme, zda číso není záporné
            raise ValueError
        self.__volume = volume_


class Warehouse:
    __capacity = None
    __products = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.__products = []

    def __repr__(self):
        return (f"Warehouse(capacity={self.capacity}, "
                f"products={len(self.__products)})")

    def __str__(self):
        return (f"Warehouse with capacity {self.capacity} "
                f"has {len(self.__products)} products.")

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity_):
        if not isinstance(capacity_, (int, float)):
            raise TypeError
        if capacity_ <= 0:
            raise ValueError
        self.__capacity = capacity_

    def add(self, product_):
        total_volume = sum([product.volume for product in self.__products])  # obsazená kapacita
        free_space = self.capacity - total_volume  # volné místo ve skladu
        if product_.volume <= free_space:  # pokud se produkt ještě na sklad vejde
            self.__products.append(product_)
            return free_space - product_.volume
        return -1


if __name__ == '__main__':
    warehouse = Warehouse(50)
    warehouse.add(Product("P1", 13.75))
    warehouse.add(Product("P2", 2.15))
    print(warehouse.add(Product("P3", 30)))
    #print(warehouse.add(Product("P4", 5)))
    print(warehouse)
