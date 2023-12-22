import csv
import json
from datetime import datetime

# Load the data from the JSON file
with open('all_repo_data.json', 'r') as f:
    data = json.load(f)

# Prepare the data for the CSV file
csv_data = []
for item in data:
    repo_last_update = datetime.strptime(item['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    week_number = repo_last_update.isocalendar()[1]
    year_number = repo_last_update.isocalendar()[0]
    key = f"{year_number}-{week_number}"
    csv_data.append({'URL': item['html_url'], 'Last Updated Week': key})

# Write the data to a CSV file
with open('repo_urls_and_weeks.csv', 'w', newline='') as csvfile:
    fieldnames = ['URL', 'Last Updated Week']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print("Data written to repo_urls_and_weeks.csv")