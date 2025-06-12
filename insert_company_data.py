import os
import django
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from jobs.models import Company

# Path to your Excel file
excel_file = r"D:\Job Portal\CompanyInfo.xlsx"

# Read the Excel file
data = pd.read_excel(excel_file)

successful = 0
failed = 0

# Iterate through each row in the Excel file
for index, row in data.iterrows():
    try:
        
        company = Company(
            name=row['Name'],  
            description=row['Description'],  
            location=row['Location'],  
            website=row.get('Website', None),  
            mobile_number=row.get('Mobile Number', None),
            email_address=row.get('Email', None) ,
            logo_url = row.get('logo_url', None),
            linkedin_url = row.get('linkedin_url', None),
            facebook_url = row . get('facebook_url', None),
            twitter_url = row.get('twitter_url', None),
            instagram_url = row.get('instagram_url', None)
        )
        company.save()
        successful += 1
    except Exception as e:
        print(f"Failed to insert row {index}: {e}")
        failed += 1

print(f"Successfully inserted {successful} rows. Failed to insert {failed} rows.")


