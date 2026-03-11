print("Hi, Welcome Mall Store")
from Register_sales import register_sales
from totals import calculate_totals
from Summary import show_summary


sales = register_sales()
total = calculate_totals(sales)
show_summary(sales, total)

