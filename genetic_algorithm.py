import random
from product import Product


def fitness(chromosome: list[str], products: list[Product], user_request: dict) -> float:
    """
    Calculate deviation of chromosome price from user budget
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


def generate_random_chromosome(product_tree: dict[str, list[Product]], user_categories: tuple[str]) -> list[str]:
    """
    Create list of random product models for user request
    :param product_tree: dict of category to products
    :param user_categories: what user choose
    :return: list of strings (chromosome)
    """
    chromosome = []
    for category in user_categories:
        random_product = random.choice(product_tree[category])
        chromosome.append(random_product.model)
    return chromosome


def genetic_algorithm(
        products: list[Product], product_tree: dict[str, list[Product]], user_request: dict
) -> list[str]:
    """
    Calculate best fitted combination of product models corresponding to user budget and number of chosen categories
    :param products:
    :param product_tree:
    :param user_request:
    :return:
    """
    population_size = 100
    user_categories = tuple(user_request['category_qty'].keys())
    initial_population = [
        generate_random_chromosome(product_tree, user_categories) for _ in range(population_size)
    ]
    fitnesses = [
        fitness(chromosome, products, user_request) for chromosome in initial_population
    ]
    # Fast variant. Todo: full genetic algo
    best_chromosome = sorted(zip(fitnesses, initial_population), key=lambda fit_pop: fit_pop[0])[0]
    return best_chromosome
