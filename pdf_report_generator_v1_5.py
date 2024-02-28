# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:28:42 2024

@author: ricardot
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:42:41 2024

@author: ricardot
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:09:47 2024

@author: ricardot
"""
import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import Tk, filedialog

def pdf_report(csv_filename, metal_name):
    
    #Create Tkinter root window
    
    root = Tk()
    root.withdraw() #Hide the root window
    
    #Open file dialog to select CSV
    csv_filename = filedialog.askopenfilename(
        title = "Select your CSV file",
        filetypes = [("CSV files", "*.csv"),("All files","*.*")])
                
    #Check if user selected a file
    if not csv_filename:
        print("No file selected. Exiting...")
        return
    
    # Read CSV file into DataFrame
    df=pd.read_csv(csv_filename)
    
    
    
    
          
    # Extract month from the first date in the DataFrame       
    month = datetime.strptime(df['Date'].iloc[0], '%d.%m.%Y').strftime('%B')
    
    #Extraxt the machine name from the DataFrame
    machine = df['Machine'].iloc[0]
    
    
    #Prepare file name
    pdf_filename = f'{metal_name}_{month}_{machine}_Usage_Report.pdf'
    
    
    #Create pdf canvas
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    
    
    #Set title and month
    
    title = f'{metal_name} Usage Report'
    c.setFont('Times-Bold', 18)
    c.drawCentredString(300, 750, title)
    c.setFont('Times-Roman', 16)
    c.drawString(50, 720, f'Month:{month}')
    
     
    #Define column headers
    columns = ["Date", "User", "Project", "Amount (nm)", "Machine"]
    
    
    #Add column headers to PDF
    col_withs = [80,80,120,100,80]
    row_height = 20
    x= 50
    y = 650
    
    
    for col_index, col_name in enumerate(columns):
        c.drawString(x, y, col_name)
        x += col_withs[col_index]
        
        
   #Add data to PDF
    y -= row_height
    for idx, row in df.iterrows():
        x = 50
        for col_index, col_name in enumerate(columns):
            if col_name == "Project":
                col_value = str(row["Project"]).zfill(4) # Fetch project number from the current row and Ensure leading zeros are preserved
            else:
                col_value = row[col_name]            
            c.drawString(x, y, str(col_value))
            x += col_withs[col_index]
        y -= row_height
        
        
    #Save PDF
    c.save()
    print(f"PDF report'{pdf_filename}' generated successfully")
       
#Test the function
#pdf_report()



