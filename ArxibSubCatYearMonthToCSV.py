import requests
from bs4 import BeautifulSoup
import csv
import re  # Import regular expressions

def fetch_arxiv_data(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')

    # Find all paper entries
    entries = page.find_all('dt')
    data = []

    for entry in entries:
        paper_link_tag = entry.find('a', title="Abstract")
        if paper_link_tag:
            paper_url = 'https://arxiv.org' + paper_link_tag['href']
            title = entry.find_next_sibling('dd').find('div', class_='list-title').text.replace('Title:', '').strip()
            authors = entry.find_next_sibling('dd').find('div', class_='list-authors').text.replace('Authors:', '').strip()
            # Fetch abstract and date from the paper's page
            abstract, submit_date = fetch_abstract_and_date(paper_url)
            data.append({
                'title': title,
                'authors': authors,
                'submit_date': submit_date,
                'abstract': abstract,
                'paper_link': paper_url
            })
    return data

def fetch_abstract_and_date(paper_url):
    response = requests.get(paper_url)
    paper_page = BeautifulSoup(response.text, 'html.parser')
    abstract = paper_page.find('blockquote', class_='abstract').text.replace('Abstract:', '').strip()
    date_line = paper_page.find('div', class_='dateline').text.strip()

    # Extract the first submission date
    match = re.search(r'\[Submitted on (\d{1,2} \w+ \d{4})', date_line)
    if match:
        submit_date = match.group(1)
    else:
        submit_date = 'Unknown'  # In case no date is found

    return abstract, submit_date

# Main URL of recent computer vision papers on arXiv
url = 'https://arxiv.org/list/cs.CV/2405?skip=0&show=2000' # cs.CV sub-category, Year 2024, Month 05 (May)
papers_data = fetch_arxiv_data(url)

csv_filename = 'arxiv_papers.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'paper_link', 'submit_date', 'authors', 'abstract']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for paper in papers_data:
        writer.writerow(paper)

print(f"Data exported to {csv_filename} successfully.")
