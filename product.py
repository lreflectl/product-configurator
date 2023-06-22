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


def generate_product_tree(products: list[Product], categories: tuple[str]) -> dict[str, list[Product]]:
    """
    Creates a tree of products by categories
    :param categories: get from db
    :param products: list of products
    :return: category to product-list dict
    """
    product_tree = {category: [] for category in categories}
    for product in products:
        product_tree[product.category].append(product)
    for cat_products in product_tree.values():
        if not cat_products:
            raise Exception('There is no products in db for this category!')
    return product_tree
