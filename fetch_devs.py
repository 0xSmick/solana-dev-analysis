import requests
from datetime import datetime
import time
import json

query = 'solana in:readme OR metaplex in:readme'
base_url = "https://api.github.com/search/repositories"
weeks_dict = {}
all_data = []

page = 1
while True:
	print('fetching page', page)
	try:
		url = f"{base_url}?q={query}&sort=updated&order=desc&page={page}"
		response = requests.get(url)
		data = response.json()

		if 'items' not in data:
			break  

		all_data.extend(data['items'])

		for repo in data['items']:
			repo_last_update = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
			week_number = repo_last_update.isocalendar()[1]
			year_number = repo_last_update.isocalendar()[0]
			
			key = f"{year_number}-{week_number}"

			if key not in weeks_dict:
				weeks_dict[key] = 0

			weeks_dict[key] += 1

		# Write the weeks data to a JSON file
		with open('repo_weeks_data.json', 'w') as f:
			json.dump(weeks_dict, f)

		# Write all the response data to a JSON file
		with open('all_repo_data.json', 'w') as f:
			json.dump(all_data, f)

		page += 1

		# Pause for 6 seconds to avoid hitting the rate limit
		time.sleep(6)

	except Exception as e:
		print(f"An error occurred: {e}")
		print(f"Retrying page {page} after 60 seconds...")
		time.sleep(60)

print("Data written to repo_weeks_data.json and all_repo_data.json")