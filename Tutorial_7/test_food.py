from food_order import calculate_total

def test_order1():
    assert calculate_total(10, 2) == 20

def test_order_30():
    # test if total food order is equal to 30
    assert calculate_total(15, 2) == 30

def test_order_100():
    # test if total food order is equal to 100
    assert calculate_total(25, 4) == 100

def test_order_10():
    # test if total food order is equal to 10
    assert calculate_total(10, 1) == 10

def test_invalid_price():
    # test if total food order is equal to "invalid price"
    assert calculate_total(-5, 2) == "invalid price"
    assert calculate_total(0, 5) == "invalid price"

def test_invalid_quantity():
    # test if total food order is equal to "invalid quantity"
    assert calculate_total(10, -1) == "invalid quantity"
    assert calculate_total(10, 0) == "invalid quantity"