import requests

# Replace with your GitHub access token
token = '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'

# API endpoint to get your repositories
url = 'https://api.github.com/user/repos'

# Set up headers with the token
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

    # Append only public repositories to the list
    public_repos = [repo for repo in data if not repo['private']]
    repos.extend(public_repos)
    page += 1

# Display repository full names
for repo in repos:
    print(f"- {repo['full_name']}")
