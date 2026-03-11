def show_summary(sales, total):

    print("SALES SUMMARY")

    for sale in sales:
        print("Product:", sale["product"])
        print("Quantity sold:", sale["quantity"])
        print()

    print("Total revenue:", total)