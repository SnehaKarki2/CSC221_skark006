import requests
import plotly.express as px

# Define the API endpoint and query parameters.
api_url = "https://api.github.com/search/repositories"
query = "?q=language:ruby+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# Make the API call.
response = requests.get(api_url + query, headers=headers)
print(f"Status code: {response.status_code}")

# Parse the JSON response.
data = response.json()
print(f"Complete results: {not data['incomplete_results']}")

# Extract repository information.
repo_items = data['items']
repo_links = []
stars = []
hover_texts = []

for repo in repo_items:
    # Create active links for repository names.
    name = repo['name']
    url = repo['html_url']
    link = f"<a href='{url}'>{name}</a>"
    repo_links.append(link)

    # Append star counts.
    stars.append(repo['stargazers_count'])

    # Create hover text.
    owner = repo['owner']['login']
    description = repo['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Generate the visualization.
title = "Most-Starred Ruby Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Customize layout.
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Customize traces.
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Display the figure.
fig.show()
