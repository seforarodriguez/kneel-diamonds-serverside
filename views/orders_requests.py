import sqlite3
import json
from models import Order
from models import styles
from models.metals import Metal
from models.sizes import Size
from models.styles import Style


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp,
            m.metal,
            m.price metal_price,
            st.style,
            st.price style_price,
            si.carets,
            si.price size_price
             -- You select the rest of the columns from the joined tables here
        FROM `Order` o
        JOIN Metal m ON m.id = o.metal_id
        JOIN Style st ON st.id = o.style_id
        JOIN Size si ON si.id = o.size_id
        """)

        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row
            order = Order(row['id'], row['metal_id'],
                    row['size_id'], row['style_id'], row['timestamp'])
            metal = Metal(row['metal_id'], row['metal'], row['metal_price'])
            style = Style(row['style_id'], row['style'], row['style_price'])
            size = Size(row['size_id'], row['carets'], row['si.price'])
            # Add the dictionary representation of the order to the list
            
            order.metal = metal.__dict__
            order.style = style.__dict__
            order.size = size.__dict__

            orders.append(order.__dict__)
          

    return orders

# Function with a single parameter


def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM `Order` o
        WHERE o.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an order instance from the current row
        # Create an order instance from the current row
        order = Order(data['id'], data['metal_id'],
                      data['size_id'], data['style_id'], data['timestamp'])

        return order.__dict__


def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Order
            ( metal_id, size_id, style_id, timestamp )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_order['metal_id'], new_order['size_id'],
              new_order['style_id'], new_order['timestamp'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id

    return new_order


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM `Order`
        WHERE id = ?
        """, (id, ))


# def update_order(id, new_order):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         UPDATE order
#             SET
#                 o.id= ?
#                 o.metal_id = ?
#                 o.size_id = ?
#                 o.style_id = ?
#                 o.timestamp = ?
#         WHERE id = ?
#         """, (new_order['metal_id'], new_order['size_id'],
#               new_order['style_id'], new_order['timestamp'], id, ))

#         # Were any rows affected?
#         # Did the client send an `id` that exists?
#         rows_affected = db_cursor.rowcount

#     if rows_affected == 0:
#         # Forces 404 response by main module
#         return False
#     else:
#         # Forces 204 response by main module
#         return True
