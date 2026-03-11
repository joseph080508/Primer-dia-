def calculate_totals(sales):
    total = 0

    for sale in sales:
        total = total + (sale["price"] * sale["quantity"])

    return total