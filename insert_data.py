import os
import django
import pandas as pd
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from jobs.models import Job, Company

excel_file = r"D:\Job Portal\JobsData_New_Part_1.xlsx"
data = pd.read_excel(excel_file)

successful = 0
failed = 0

for index, row in data.iterrows():
    try:
        # Get or create the company
        company_name = row['company']
        company, created = Company.objects.get_or_create(name=company_name)

        # Insert the job
        job = Job.objects.create(
            title=row['title'],
            company=company,
            job_type=row['job_type'],
            skills_required=row['skills_required'],
            description=row['description'],
            location=row['location'],
            date_posted=pd.to_datetime(row['date_posted']).to_pydatetime(),
            experience_required=row.get('experience_required', None),
            application_link = row.get('application_link', None)
        )
        successful += 1
    except Exception as e:
        print(f"Error inserting row {index}: {e}")
        failed += 1

print(f"Successfully inserted {successful} rows. Failed to insert {failed} rows.")
