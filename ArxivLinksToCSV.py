import requests
from bs4 import BeautifulSoup
import csv
import re  # Import regular expressions

def fetch_paper_details(urls):
    data = []
    for url in urls:
        response = requests.get(url)
        page = BeautifulSoup(response.text, 'html.parser')

        title = page.find('h1', class_='title').text.replace('Title:', '').strip()
        authors = page.find('div', class_='authors').text.replace('Authors:', '').strip()
        date_line = page.find('div', class_='dateline').text.strip()

        # Extract the first submission date
        match = re.search(r'\[Submitted on (\d{1,2} \w+ \d{4})', date_line)
        if match:
            submit_date = match.group(1)
        else:
            submit_date = 'Unknown'  # In case no date is found

        data.append({
            'title': title,
            'authors': authors,
            'submit_date': submit_date,
            'paper_link': url
        })

    return data

def save_to_csv(papers_data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link', 'Date', 'Authors'])
        for paper in papers_data:
            writer.writerow([paper['title'], paper['paper_link'], paper['submit_date'], paper['authors']])

# List of arXiv URLs
arxiv_urls = ['https://arxiv.org/abs/1606.03498',
 'https://arxiv.org/abs/1706.08500',
 'https://arxiv.org/abs/1801.01401',
 'https://arxiv.org/abs/2203.06026']

papers_data = fetch_paper_details(arxiv_urls)
save_to_csv(papers_data, 'arxiv_papers.csv')

print("Data has been saved to 'arxiv_papers.csv'.")
