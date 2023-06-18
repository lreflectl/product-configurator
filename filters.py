from product import Product


def filter_color(products: list[Product], color: str):
    return [product for product in products if product.color == color]


def filter_collection(products: list[Product], collection: str):
    return [product for product in products if product.collection == collection]
