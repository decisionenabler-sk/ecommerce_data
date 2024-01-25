from data_loader import load_data
from datetime import datetime
ecommerce_data = load_data()
def calculate_avg_delivery_time(ecommerce_data):

    for order in ecommerce_data["orders"]:
        start = order["order_date"]
        print(start)
    for delivery in ecommerce_data["deliveries"]:
        delivery_status = delivery["status"]
        end = delivery["delivery_date"]
        print(end)
    
calculate_avg_delivery_time(ecommerce_data)
