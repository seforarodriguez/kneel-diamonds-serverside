ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "timestamp": 1614659931693
    },{
        "id": 2,
        "metalId": 1,
        "sizeId": 1,
        "styleId": 1,
        "timestamp": 1614659931694
    },{
        "id": 3,
        "metalId": 2,
        "sizeId": 3,
        "styleId": 3,
        "timestamp": 1614659931695
    },{
        "id": 4,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 2,
        "timestamp": 1614659931696
    }
]


def get_all_orders():
    return ORDERS

# Function with a single parameter


def get_single_order(id):
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order
    return requested_order


def create_order(order):
    # Get the id value of the last animal in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    order_index = -1
   # Iterate the ANIMALS list, but use enumerate() so that you
   # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Store the current index.
            order_index = index

    # If the animal was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    # Iterate the orderS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
