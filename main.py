import json
from product import Product, generate_product_tree
from filters import filter_color, filter_collection
from genetic_algorithm import fitness, generate_random_chromosome


def main():
    products = []
    with open('example_data.json') as file:
        data = json.load(file)
        for prod_data in data['products']:
            products.append(Product(**prod_data))

    user_request = {
        'color': 'green',
        'collection': 'roman',
        'category_qty': {
            'chandelier': 6,
            'switch': 10
        },
        'budget': 5000,
    }

    products = filter_color(products, user_request['color'])
    products = filter_collection(products, user_request['collection'])

    user_categories = list(user_request['category_qty'].keys())
    product_tree = generate_product_tree(products, user_categories)
    print(product_tree)

    chromosome = generate_random_chromosome(product_tree, user_categories)
    print(chromosome)

    print(fitness(chromosome, products, user_request))


if __name__ == '__main__':
    main()
