# product.py

def get_product_info(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )

# Demo run (optional)
if _name_ == "_main_":
    result = get_product_info("P101", "Keyboard", 5, 750)
    print(result)
