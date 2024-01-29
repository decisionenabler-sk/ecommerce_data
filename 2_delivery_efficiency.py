from data_loader import load_data
from datetime import timedelta
import pandas as pd
ecommerce_data = load_data()
# this type of problem will be easily solved by pandas

def calculate_average_delivery_time(data):
    # Create DataFrame for orders
    orders_df = pd.DataFrame(data["orders"])

    # Create DataFrame for deliveries
    deliveries_df = pd.DataFrame(data["deliveries"])

    # Merge orders and deliveries on order_id
    merged_df = pd.merge(deliveries_df, orders_df, on="order_id")

    # Convert date strings to datetime objects
    merged_df["order_date"] = pd.to_datetime(merged_df["order_date"])
    merged_df["delivery_date"] = pd.to_datetime(merged_df["delivery_date"])

    # Calculate delivery time
    merged_df["delivery_time"] = merged_df["delivery_date"] - merged_df["order_date"]

    # Calculate average delivery time for each status
    average_times = merged_df.groupby("status")["delivery_time"].mean().dt.total_seconds().apply(lambda x: str(timedelta(seconds=x))).to_dict()

    return average_times

# Example usage:

result = calculate_average_delivery_time(ecommerce_data)
print(result)

