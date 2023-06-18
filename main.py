import json
from product import Product
from filters import filter_color, filter_collection
from genetic_algorithm import fitness


def main():
    products = []
    with open('example_data.json') as file:
        data = json.load(file)
        for prod_data in data['products']:
            products.append(Product(**prod_data))

    products = filter_color(products, 'green')
    products = filter_collection(products, 'roman')
    print(products)

    # todo: put in json
    user_request = {
        'category_qty': {
            'chandelier': 6,
            'switch': 10
        },
        'budget': 5000,
    }

    print(fitness(['model 234', 'model 516'], products, user_request))


if __name__ == '__main__':
    main()
