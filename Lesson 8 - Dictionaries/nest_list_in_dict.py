pizzas = {
    'pizza1': {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        'price': 24.99
    },

    'pizza2': {
        'crust': 'thin',
        'toppings': ['mushrooms', 'extra cheese', 'salami'],
        'price': 54.99
    }
}


for pizza in pizzas.items():
    # print(f'You ordered a pizza {item} with {item[0]} crust \
    #     with following toppings {item[1]}\nCost: ${item[2]}')
    print(pizza)
        

