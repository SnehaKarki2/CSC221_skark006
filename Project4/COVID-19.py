import requests
import plotly.graph_objs as go
from plotly.offline import plot

# Function to fetch COVID-19 data for a list of countries
def fetch_covid_data(countries):
    covid_data = []
    base_url = "https://disease.sh/v3/covid-19/countries/"
    for country in countries:
        response = requests.get(base_url + country)
        if response.status_code == 200:
            data = response.json()
            country_data = {
                'country': country,
                'cases': data['cases'],
                'deaths': data['deaths'],
                'recovered': data['recovered']
            }
            covid_data.append(country_data)
        else:
            print(f"Failed to fetch data for {country}. Status code: {response.status_code}")
    return covid_data

# Function to visualize the COVID-19 data using Plotly
def visualize_covid_data(covid_data):
    countries = [data['country'] for data in covid_data]
    cases = [data['cases'] for data in covid_data]
    deaths = [data['deaths'] for data in covid_data]
    recovered = [data['recovered'] for data in covid_data]

    # Create a bar chart for cases
    cases_trace = go.Bar(
        x=countries,
        y=cases,
        name='Cases',
        marker=dict(color='rgba(255, 165, 0, 0.6)')
    )

    # Create a bar chart for deaths
    deaths_trace = go.Bar(
        x=countries,
        y=deaths,
        name='Deaths',
        marker=dict(color='rgba(255, 99, 71, 0.6)')
    )

    # Create a bar chart for recovered
    recovered_trace = go.Bar(
        x=countries,
        y=recovered,
        name='Recovered',
        marker=dict(color='rgba(0, 128, 0, 0.6)')
    )

    data = [cases_trace, deaths_trace, recovered_trace]

    layout = go.Layout(
        title='COVID-19 Data for Multiple Countries',
        xaxis=dict(title='Country'),
        yaxis=dict(title='Number of People'),
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='covid_data.html')

# Main code
if __name__ == "__main__":
    countries = ['USA', 'India', 'Brazil', 'France', 'Russia', 'UK', 'Italy', 'Germany']
    covid_data = fetch_covid_data(countries)
    visualize_covid_data(covid_data)
