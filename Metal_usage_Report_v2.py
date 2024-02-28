# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:22:10 2024

@author: ricardot
"""

from Data_Input import get_metal_usage
from Save_to_CSV import save_to_csv
from pdf_report_generator_v1_5 import pdf_report

def main():
    metal_usage_list = []  # Empty list to store the Dict information

    while True:
        usage = get_metal_usage() 

        if usage is not None:
            print("Data entered successfully", usage)
            metal_usage_list.append(usage)  # Append every new line of data
        else:
            print("Error in input. Please try again")

        another_entry = input("Do you want to enter another record? (y/n): ").lower()
        if another_entry == 'n':
            print("Exiting program.")
            break
        elif another_entry != 'y':
            print("Invalid input. Please enter 'y' or 'n'.")

    print("\nCollected Data:")
    for i in metal_usage_list:
        print(i)

    # Save metal usage data to a CSV file
    save_to_csv(metal_usage_list)
    
    # Save metal usage data to a CSV file and get the generated filename
    csv_filename = save_to_csv(metal_usage_list)
    
    # Extract metal name from the first record
    metal_name = metal_usage_list[0]["metal"]

    # Generate PDF report
    #csv_filename = f"{metal_usage_list[0]['metal']}_{metal_usage_list[0]['date'].strftime('%B')}_{metal_usage_list[0]['machine']}.csv"
    pdf_report(csv_filename,metal_name)


if __name__ == "__main__":
    main()




