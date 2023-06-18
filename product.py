from dataclasses import dataclass


@dataclass
class Product:
    model: str
    category: str
    collection: str
    color: str
    price: int
    quantity: int

    def __repr__(self):
        return f'{self.model} ({self.price} UAH, {self.quantity} pcs)'
