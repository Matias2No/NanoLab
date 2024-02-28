# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:20:56 2024

@author: ricardot
"""

import csv

def save_to_csv(data_list):
    metal = data_list[0]["metal"]
    month = data_list[0]["date"].strftime("%B")  # Get full month name
    machine = data_list[0]["machine"]

    # Generate filename based on input data
    filename = f"{metal}_{month}_{machine}.csv"

    # Define column names for the CSV file
    columns = ["Date", "User", "Project", "Amount (nm)", "Machine"]

    # Write data to CSV file
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for record in data_list:
            # Create a new dictionary with keys matching fieldnames
            row_data = {
                "Date": record["date"].strftime('%d.%m.%Y'),  # Format date before writing
                "User": record["user"],
                "Project": record["project"],
                "Amount (nm)": record["amount"],
                "Machine": record["machine"]
            }
            writer.writerow(row_data)

    print(f"Metal usage data saved to '{filename}'")
