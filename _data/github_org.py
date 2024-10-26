import requests

# Replace with your organization name and access token
org_name = 'Computer-Engineering-Department-Archive'
token = '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'

# API endpoint for listing org repositories
url = f'https://api.github.com/orgs/{org_name}/repos'

# Set up the headers with the token
headers = {
    'Authorization': f'token {token}'
}

# Making the API request
repos = []
page = 1

while True:
    response = requests.get(url, headers=headers, params={'page': page, 'per_page': 100})
    data = response.json()
    
    if response.status_code != 200 or not data:
        break

    # Append the current page repos to the list
    repos.extend(data)
    page += 1

# Display repository names
for repo in repos:
    print(f'''- {repo['name']}''')
