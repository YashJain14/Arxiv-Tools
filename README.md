# Arxiv-Tools
1. [Paper Links to CSV](#arxivlinkstocsvpy)
2. [Sub-Category, Year, Month to CSV](#arxibsubcatyearmonthtocsvpy)
3. [Author List to CSV](#authorstocsvpy)



## ArxivLinksToCSV.py

**List of arXiv URLs**: Update the list of arXiv URLs in the script.

```python
arxiv_urls = [
    'https://arxiv.org/abs/1606.03498',
    'https://arxiv.org/abs/1706.08500',
    'https://arxiv.org/abs/1801.01401'
]
```


## ArxibSubCatYearMonthToCSV.py

**Update the URL**: Set the URL to the desired category, subcategory, year, and month in the script. For example:

```python
category = "cs"
subcategory = "CV"
year = "24"
month = "05"
url = f'https://arxiv.org/list/{category}.{subcategory}/{year}{month}?skip=0&show=2000' # cs.CV sub-category, Year 2024, Month 05 (May)

```


## AuthorsToCSV.py

**List of Authors**: Update the list of authors in the script as needed. The list is defined within the script as follows:

```python
authorList = [
    "Author One",
    "Author Two",
    "Author Three",
    # Add more authors as needed
]
```
><hr>
## Output

The output CSV file `arxiv_papers.csv` will have the following columns:

- Title
- Link
- Date
- Authors
- Abstract


## Example Output Structure

| Title                         | Link                        | Date       | Authors               | Abstract              |
|-------------------------------|-----------------------------|------------|-----------------------|-----------------------|
| Efficient Object Detection    | https://arxiv.org/abs/1606.03498 | 2016-06-07 | John Doe, Jane Smith  | This paper discusses... |
| Understanding GANs            | https://arxiv.org/abs/1706.08500 | 2017-06-21 | Alice Brown, Bob White| This work explores... |
| Deep Learning for NLP         | https://arxiv.org/abs/1801.01401 | 2018-01-04 | Charlie Green         | We present...           |
| Advances in Machine Learning  | https://arxiv.org/abs/2203.06026 | 2022-03-10 | David Black           | This paper proposes...  |

