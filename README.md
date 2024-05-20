# Arxiv-Tools
1. [Paper Links to CSV](#arxivlinkstocsvpy)
2. [Sub-Category, Year, Month to CSV](#arxibsubcatyearmonthtocsvpy)



## ArxivLinksToCSV.py

1. **List of arXiv URLs**: Update the list of arXiv URLs in the script.

```python
arxiv_urls = [
    'https://arxiv.org/abs/1606.03498',
    'https://arxiv.org/abs/1706.08500',
    'https://arxiv.org/abs/1801.01401'
]
```

2. **Run the script**: Execute the script to fetch paper details and save them into a CSV file.

```sh
python ArxivLinksToCSV.py
```

The script will save the paper details in a file named `arxiv_papers.csv`.

### Output

The output CSV file `arxiv_papers.csv` will have the following columns:

- Title
- Link
- Date
- Authors
- Abstract

### Example Output

| Title 	| Link 	| Date 	| Authors 	| Abstract 	|
|---	|---	|---	|---	|---	|
| Improved Techniques for Training GANs 	| https://arxiv.org/abs/1606.03498 	| 10 Jun 2016 	| Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen 	| We present a variety of new architectural features and… 	|
| GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium 	| https://arxiv.org/abs/1706.08500 	| 26 Jun 2017 	| Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter 	| Generative Adversarial Networks (GANs) excel at creating realistic images… 	|
| Demystifying MMD GANs 	| https://arxiv.org/abs/1801.01401 	| 4 Jan 2018 	| Mikołaj Bińkowski, Danica J. Sutherland, Michael Arbel, Arthur Gretton 	| We investigate the training and performance of generative adversarial… 	|

## ArxibSubCatYearMonthToCSV.py

1. **Update the URL**: Set the URL to the desired category, subcategory, year, and month in the script. For example:

```python
url = 'https://arxiv.org/list/cs.CV/2405?skip=0&show=2000' # cs.CV sub-category, Year 2024, Month 05 (May)
```

2. **Run the script**: Execute the script to fetch paper details and save them into a CSV file.

```sh
python ArxibSubCatYearMonthToCSV.py
```

The script will save the paper details in a file named `arxiv_papers.csv`.

## Output

The output CSV file `arxiv_papers.csv` will have the following columns:

- Title
- Link
- Date
- Authors
- Abstract

## Example Output

| Title                         | Link                        | Date              | Authors               | Abstract              |
|-------------------------------|-----------------------------|-------------------|-----------------------|-----------------------|
| Automatic Creative Selection with Cross-Modal Matching    | https://arxiv.org/abs/2405.00029 | 28 Feb 2024         | 28 Feb 2024	Alex Kim, Jia Huang, Rob Monarch...  | Application developers advertise their Apps by... |
| Using Texture to Classify Forests Separately from Vegetation            | https://arxiv.org/abs/2405.00264	 | 1 May 2024        | David R. Treadwell IV, Derek Jacoby... | Identifying terrain within satellite image data is a key issue... |
| CREPE: Coordinate-Aware End-to-End Document Parser         | https://arxiv.org/abs/2405.00260 | 1 May 2024         | Yamato Okamoto, Youngmin Baek, Geewook Kim...        | In this study, we formulate an OCR-free sequence generation model...          |


##### Notes
> <i>The script only fetches the latest 2000 papers of the time period