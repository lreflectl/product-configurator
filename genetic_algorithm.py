from product import Product


def fitness(chromosome: list[str], products: list[Product], user_request: dict) -> float:
    """
    :param chromosome: list of the exact models (or model ids) for every category in the request
    :param products: list (or dictionary) of product objects every of each include price, qty, model
    :param user_request: dict that has user budget and amounts of products needed in each category
    :return: float (or int) price difference between budget and chromosome`s price sum (0 is the best)
    """
    price_sum = 0
    for model in chromosome:
        product = None
        for p in products:
            if p.model == model:
                product = p
                break
        if product is not None:
            price_sum += product.price * user_request['category_qty'][product.category]
        else:
            raise Exception(f'No product with model: {model}')

    return abs(user_request['budget'] - price_sum)
