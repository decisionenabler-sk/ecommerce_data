from collections import defaultdict
from data_loader import load_data
from datetime import datetime
ecommerce_data = load_data()

# 1. we will calculate average working hours for each employee
def calculate_avg_wh_employee(data):
    total_wh = defaultdict(int)
    avg_wh = defaultdict(float)
    for employee in data["employees"]:
        for wh in employee["working_hours"]:
            total_wh[employee["name"]] += wh["hours"]
        avg_wh[employee["name"]] = total_wh[employee["name"]]/len(employee["working_hours"])
    return dict(avg_wh)
#2. we will calculate average working hours for each day (across all employees)
def calculate_avg_wh_day(data):
    total_wh = defaultdict(int)
    avg_wh = defaultdict(float)
    for employee in data["employees"]:
        for wh in employee["working_hours"]:
            day = wh["day"]
            total_wh[day] += wh["hours"]
    return dict(total_wh)
# TODO: How many employees worked on each day?

# 3. We will find the employee and day with highest average working hours
    
# Run the results
emp = calculate_avg_wh_employee(ecommerce_data)
print(emp)

day = calculate_avg_wh_day(ecommerce_data)
print(day)