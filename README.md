# Arxiv-Tools


### Usage ArxivLinksToCSV.py

1. **List of arXiv URLs**: Update the list of arXiv URLs in the script.

```python
arxiv_urls = [
    'https://arxiv.org/abs/1606.03498',
    'https://arxiv.org/abs/1706.08500',
    'https://arxiv.org/abs/1801.01401',
    'https://arxiv.org/abs/2203.06026'
]
```

2. **Run the script**: Execute the script to fetch paper details and save them into a CSV file.

```sh
python fetch_arxiv_papers.py
```

The script will save the paper details in a file named `arxiv_papers.csv`.

### Output

The output CSV file `arxiv_papers.csv` will have the following columns:

- Title
- Link
- Date
- Authors

### Example Output

|Title|Link|Date|Authors|
|---|---|---|---|
|Improved Techniques for Training GANs|https://arxiv\.org/abs/1606\.03498|10 Jun 2016|Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen|
|GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium|https://arxiv\.org/abs/1706\.08500|26 Jun 2017|Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter|
|Demystifying MMD GANs|https://arxiv\.org/abs/1801\.01401|4 Jan 2018|Mikołaj Bińkowski, Danica J\. Sutherland, Michael Arbel, Arthur Gretton|
|The Role of ImageNet Classes in Fréchet Inception Distance|https://arxiv\.org/abs/2203\.06026|11 Mar 2022|Tuomas Kynkäänniemi, Tero Karras, Miika Aittala, Timo Aila, Jaakko Lehtinen|


