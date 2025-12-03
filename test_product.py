from product import get_product_info

def test_get_product_info():
    result = get_product_info("P101", "Keyboard", 5, 750)

    expected = (
        "Product ID: P101\n"
        "Name: Keyboard\n"
        "Quantity: 5\n"
        "Price: 750"
    )

    assert result == expected
