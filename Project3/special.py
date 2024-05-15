import requests
import matplotlib.pyplot as plt

def fetch_book_counts(topic):
    url = f"https://openlibrary.org/search.json?q={topic}"
    response = requests.get(url)
    data = response.json()
    return data['numFound']

def plot_publication_counts(topic, count):
    plt.figure(figsize=(6, 4))
    plt.bar(topic, count)
    plt.title(f'Number of Books Published about {topic}')
    plt.ylabel('Number of Publications')
    plt.show()

if __name__ == "__main__":
    topic = 'Artificial Intelligence'
    books_count = fetch_book_counts(topic)
    plot_publication_counts(topic, books_count)
