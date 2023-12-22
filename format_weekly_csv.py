import csv
import json

# Load the data from the JSON file
with open('repo_weeks_data.json', 'r') as f:
    data = json.load(f)

# Sort the data in descending order by the key
sorted_data = dict(sorted(data.items(), key=lambda item: tuple(map(int, item[0].split('-'))), reverse=True))

# Write the sorted data to a CSV file
with open('repo_weeks_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Week', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key, value in sorted_data.items():
        writer.writerow({'Week': key, 'Count': value})

print("Data written to repo_weeks_data.csv")