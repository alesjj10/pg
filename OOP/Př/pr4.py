from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: int = 1000
    tags: list = field(default_factory=list)

class Product2:
    def __init__(self, name, price=1000, tags=[]):
        self.name = name
        self.price = price
        if tags is not None:
            self.tags = tags
        else:
            self.tags = []


    def __repr__(self):
        return f"Produkt2: name={self.name}, price={self.price}, tags={self.tags}"

if __name__ == "__main__":
    p1 = Product("Zubni kartacek")
    print(p1)
    p2 = Product("Zubni pasta")
    print(p2)
    p2.tags.append("matova")
    print(p2)
    print(p1)