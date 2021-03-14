

# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):  # could be anything name wise - they must make sense
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, total):
    pet_shop["admin"]["total_cash"] = total + get_total_cash(pet_shop)


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] = pets_sold + get_pets_sold(pet_shop)


def get_stock_count(pet_shop):
    total_pets = 0

    for pet in pet_shop:
        total_pets = len(pet_shop['pets'])
    return total_pets


def get_pets_by_breed(pet_shop, breed_name):
    breed_list = []

    for pet in pet_shop['pets']:
        if pet['breed'] == breed_name:
            breed_list.append(pet['breed'])
    return breed_list


def find_pet_by_name(pet_shop, pet_name):
    for name in pet_shop['pets']:
        if name['name'] == pet_name:
            return name


# def remove_pet_by_name(pet_shop, pet_name):
#     for name in pet_shop['pets']:
#         if name['name'] == pet_name:
#             del name['name']


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)


def get_customer_cash(customers):
    return customers['cash']


def remove_customer_cash(customers, cash):
    customers['cash'] = customers['cash'] - cash
    return customers['cash']


def get_customer_pet_count(customers):
    pet_list = []
    for pet in customers['pets']:
        pet_list.append(customers['pets'])
    pet_count = len(pet_list)
    return pet_count


def add_pet_to_customer(customers, new_pet):
    return customers['pets'].append(new_pet)