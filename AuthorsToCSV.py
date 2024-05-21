import requests
import csv
from bs4 import BeautifulSoup
import datetime

# List of authors to search for
authorList = [
    "Author One",
    "Author Two",
    "Author Three",
    # Add more authors as needed
]

# Arxiv API endpoint for search
arxiv_url = "http://export.arxiv.org/api/query"

def fetch_papers_by_authors(authors):
    # Get the current date
    today = datetime.datetime.now()

    # Format the date for the arxiv API query
    date = today.strftime("%Y-%m-%d")

    author_query = 'au:"{}"'.format('" OR au:"'.join(authors))

    # Send the request to the arxiv API
    response = requests.get(arxiv_url + f'?search_query={author_query}&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending')

    # Parse the XML response
    soup = BeautifulSoup(response.content, 'xml')

    # Get all the paper entries
    entries = soup.find_all('entry')

    papers = []
    # Get title, summary, author, link, date
    for entry in entries:
        title = entry.find('title').text
        abstract = entry.find('summary').text
        authors = entry.find_all('author')
        authors = [author.find('name').text for author in authors]
        link = entry.find('id').text
        date = entry.find('published').text
        papers.append({
            'title': title,
            'link': link,
            'date': date.split('T')[0],  # Format date properly
            'authors': ', '.join(authors),
            'abstract': abstract.strip()
        })

    return papers

def save_to_csv(papers, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'link', 'date', 'authors', 'abstract']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)

    print(f"Data exported to {filename} successfully.")

# Main execution
if __name__ == "__main__":
    papers_data = fetch_papers_by_authors(authorList)
    save_to_csv(papers_data, 'arxiv_papers.csv')
