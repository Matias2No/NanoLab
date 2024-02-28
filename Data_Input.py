# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:20:11 2024

@author: ricardot
"""

from datetime import datetime

def get_metal_usage():
    metal = input("Enter the metal name: ")
    machine = input("Enter the e-beam name: ")

    # Loop until a valid date is entered
    while True:
        try:
            date_str = input("Enter the date (DD.MM.YYY): ")
            date = datetime.strptime(date_str, '%d.%m.%Y').date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in DD.MM.YYYY format")

    user = input("Enter user name: ")
    project = input("Enter Project name - NL:  ")

    # Loop until a valid amount is entered    
    while True:
        try: 
            amount = int(input("Enter the amount of material used (nm): "))
            break                        
        except ValueError:
            print("Invalid amount format. Please enter a numeric value")

    data = {
        "metal": metal,
        "machine": machine,
        "date": date,
        "user": user,
        "project": project,
        "amount": amount
    }

    return data
