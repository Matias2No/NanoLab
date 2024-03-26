# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:37:22 2024

@author: ricardot
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
from metal_usage_app import Ui_MainWindow
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.setWindowTitle("Monthly Usage")
        self.ui.save_data.clicked.connect(self.f_save_data)
        self.ui.csv.clicked.connect(self.save_to_csv)
        self.data = []

    def f_save_data(self):
        # Extracts data from GUI
        metal = self.ui.comboBox_2.currentText()
        machine = self.ui.comboBox.currentText()
        user = self.ui.lineEdit_user.text()
        project = self.ui.lineEdit_Project.text()
        amount = int(self.ui.lineEdit_amaunt.text())
        
        # Extracts the date
        sel_date = self.ui.dateEdit.date().toPyDate()
        
        # Creating the data dict
        data = {           
            "metal": metal,
            "machine": machine,
            "date": sel_date,
            "user": user,
            "project": project,
            "amount": amount
        }
        
        # Append the data to the list
        self.data.append(data)
        
        # Clear input fields
        self.ui.lineEdit_user.clear()
        self.ui.lineEdit_Project.clear()
        self.ui.lineEdit_amaunt.clear()
        
        # Show confirmation message
        QMessageBox.information(self, "Success", "Data entered successfully.")

    def save_to_csv(self):
        if self.data:
            # Ask user for confirmation
            reply = QMessageBox.question(self, 'Confirmation', 
                                         'Do you want to save the data to CSV file?', 
                                         QMessageBox.Yes | QMessageBox.No, 
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Generate filename based on input data
                metal = self.data[0]["metal"]
                month = self.data[0]["date"].strftime("%B")  # Get full month name
                machine = self.data[0]["machine"]
                filename = f"{metal}_{month}_{machine}.csv"

                # Define column names for the CSV file
                columns = ["Date", "User", "Project", "Amount (nm)", "Machine"]

                # Write data to CSV file
                with open(filename, "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=columns)
                    writer.writeheader()
                    for data in self.data:
                        writer.writerow({
                            "Date": data["date"].strftime('%d.%m.%Y'),
                            "User": data["user"],
                            "Project": data["project"],
                            "Amount (nm)": data["amount"],
                            "Machine": data["machine"]
                        })

                QMessageBox.information(self, "Success", f"Metal usage data saved to '{filename}'")
                self.data = []  # Clear the data list after saving to CSV
        else:
            QMessageBox.warning(self, "No Data", "No data available to save to CSV.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



