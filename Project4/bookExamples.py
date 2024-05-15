import requests

# Define the API endpoint and query parameters.
api_url = "https://api.github.com/search/repositories"
query = "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# Make the API call.
response = requests.get(api_url + query, headers=headers)
print(f"Status code: {response.status_code}")

# Parse the JSON response.
data = response.json()

# Display summary information.
total_repos = data['total_count']
incomplete_results = data['incomplete_results']
print(f"Total repositories: {total_repos}")
print(f"Complete results: {not incomplete_results}")

# Get the list of repositories.
repositories = data['items']
print(f"Repositories returned: {len(repositories)}")

# Display selected information for each repository.
print("\nSelected information about each repository:")
for repo in repositories:
    repo_name = repo['name']
    owner_name = repo['owner']['login']
    stars = repo['stargazers_count']
    repo_url = repo['html_url']
    created_at = repo['created_at']
    updated_at = repo['updated_at']
    description = repo['description']

    print(f"Name: {repo_name}")
    print(f"Owner: {owner_name}")
    print(f"Stars: {stars}")
    print(f"Repository URL: {repo_url}")
    print(f"Created: {created_at}")
    print(f"Updated: {updated_at}")
    print(f"Description: {description}\n")
