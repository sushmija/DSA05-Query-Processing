import pandas as pd
file_path='employee.csv'
employee_jobs=pd.read_csv(file_path)
more_job=employee_jobs.groupby('EMPLOYEE_ID').filter(lambda x: len(x) >= 2)
print("Employees with Two or More Jobs:",more_job)
