from collections import defaultdict
from data_loader import load_data
from datetime import datetime
ecommerce_data = load_data()
import datetime


def identify_late_deliveries(data):

  late_deliveries = []
  for order in data["orders"]:
    order_id = order["order_id"]
    expected_delivery_date = datetime.datetime.strptime(order["order_date"], "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(days=3)

    for delivery in data["deliveries"]:
      if delivery["order_id"] == order_id:
        actual_delivery_date = datetime.datetime.strptime(delivery["delivery_date"], "%Y-%m-%dT%H:%M:%S")
        if actual_delivery_date > expected_delivery_date:
          late_delivery = {
            "order_id": order_id,
            "expected_delivery_date": expected_delivery_date.strftime("%Y-%m-%d"),
            "actual_delivery_date": actual_delivery_date.strftime("%Y-%m-%d"),
          }

          # Identify possible reasons for delay based on available data
          delivery_person_id = delivery["delivery_person_id"]
          for employee in data["employees"]:
            if employee["employee_id"] == delivery_person_id:
              # Check if the delivery person had enough working hours on the delivery day
              for working_hour in employee["working_hours"]:
                if working_hour["day"] == actual_delivery_date.strftime("%Y-%m-%d"):
                  if working_hour["hours"] < 8:
                    late_delivery["reason_for_delay"] = "Delivery person might not have had enough working hours on the delivery day."
                    late_delivery["suggested_improvement"] = "Ensure delivery person has sufficient working hours allocated for the expected delivery date."
                  break

          late_deliveries.append(late_delivery)

  return late_deliveries


late_deliveries = identify_late_deliveries(ecommerce_data)

if late_deliveries:
  print("Late deliveries:")
  for delivery in late_deliveries:
    print(f"Order ID: {delivery['order_id']}")
    print(f"Expected delivery date: {delivery['expected_delivery_date']}")
    print(f"Actual delivery date: {delivery['actual_delivery_date']}")
    if "reason_for_delay" in delivery:
      print(f"Reason for delay: {delivery['reason_for_delay']}")
    if "suggested_improvement" in delivery:
      print(f"Suggested improvement: {delivery['suggested_improvement']}")
    print("---")
else:
  print("No late deliveries found.")

