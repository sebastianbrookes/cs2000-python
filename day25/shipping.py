def shipping_cost(weight: int) -> int:
    """if weight <= 1, cost is $5; if weight <= 5, cost is $10; otherwise, $20"""
    if weight <= 1:
        return 5
    elif weight <= 5:
        retrun 10
    else:
        return 20
 
print(shipping_cost(3))