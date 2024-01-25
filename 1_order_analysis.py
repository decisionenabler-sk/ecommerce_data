from collections import defaultdict
from data_loader import load_data
ecommerce_data = load_data()
def top_purchases(ecommerce_data):
    # 1. we need to find top selling products by calculating total quantity by product_id
    # clarifying question: How do we define top selling products?
    product_sale = defaultdict(int)
    customer_total_amount = defaultdict(float)
    for order in ecommerce_data["orders"]:
        for item in order["items"]:
            product_sale[item["product_id"]] += item["quantity"]
    # 2. We need to calculate total amount of purchase by customer_id and return the highest purchase
    # clarifying question: in case of a tie, do we return all the customers?     
        customer_total_amount[order["order_id"]] += order["total_amount"]
    # print(dict(product_sale))
    # print(dict(customer_total_amount))
    top_products = [key for key,value in product_sale.items() if value == max(product_sale.values())]
    highest_purchase_customers = [key for key,value in customer_total_amount.items() if value == max(customer_total_amount.values())]
    return top_products, highest_purchase_customers

print("The product(s) that were sold most are:",top_purchases(ecommerce_data)[0])
print("The customer(s) who made the highest purchase are:", top_purchases(ecommerce_data)[1])