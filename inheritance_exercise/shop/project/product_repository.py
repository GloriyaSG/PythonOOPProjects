from project.product import Product
from typing import List, Optional


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        res = [prod for prod in self.products if prod.name == product_name]
        if res:
            return res[0]

    def remove(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)

    def __repr__(self):
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])

