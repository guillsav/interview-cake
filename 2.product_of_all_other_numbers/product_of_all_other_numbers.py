# O(?) time | O(?) space
def get_products_of_all_ints_except_at_index(int_list: list) -> list:

    if len(int_list) < 2:
        raise IndexError(
            "Getting the product of numbers at other indices requires at least 2 numbers")

    # We make a list with the length of the input list to
    # hold our products
    product_list = [None]*len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product = 1
    for i in range(len(int_list)):
        product_list[i] = product
        product *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product = 1
    for i in range(len(int_list) - 1, -1, -1):
        product_list[i] *= product
        product *= int_list[i]

    return product_list
