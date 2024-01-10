import pandas as pd
file_path = 'JobTitle.csv'
jobs = pd.read_csv(file_path)
sorted_jobs=jobs.sort_values(by='JOB_TITLE',ascending=False)
print("Details of Jobs in descending sequence on job title",sorted_jobs)
