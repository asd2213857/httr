# HTML Table to CSV Converter

This Python package provides a function to convert HTML tables into CSV format using BeautifulSoup. The function `html_table_to_rows` extracts data from an HTML table and formats it into rows suitable for conversion to CSV.

## Requirements

- Python 3.x
- BeautifulSoup4
- pandas (option)

## Installation

Install the required packages using pip:

```bash
pip install beautifulsoup4
pip install pandas
```

## Usage
Here is an example of how to use the html_table_to_rows function to convert an HTML table to a CSV format:
 
### Function: `html_table_to_rows`
This function takes an HTML table and a list of strings to be replaced from the table cells, and returns a list of rows representing the CSV content.
``` python
def html_table_to_rows(table_soup, replace_str_list):
    rows = table_soup.find_all('tr')
    csv_rows = []
    for row in rows:
        csv_row = []
        if row.select("th,td"):
            for cell in row.select("th,td"):
                col_span = int(cell.get("colspan",1))
                cell_content = cell.text
                for replace_str in replace_str_list:
                    cell_content = cell_content.replace(replace_str, "")
                cell_content = cell_content.strip()
                csv_row+=[cell_content]*col_span
        if csv_row:
            csv_rows.append(csv_row)
    return csv_rows
```

### Example Code
Below is an example of how to use the html_table_to_rows function to convert an HTML table to a pandas DataFrame:


```python
import pandas as pd
from bs4 import BeautifulSoup

html_content = """
<table>
  <tr><th>Header 1</th><th>Header 2</th></tr>
  <tr><td>Row 1, Col 1</td><td>Row 1, Col 2</td></tr>
  <tr><td>Row 2, Col 1</td><td>Row 2, Col 2</td></tr>
</table>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Replace strings list
replace_str_list = ["..."]

# Extract the first table from the HTML content
table_soup = soup.find_all("table")[0]

# Convert the HTML table to CSV rows
csv_rows = html_table_to_rows(table_soup, replace_str_list)

# Create a pandas DataFrame from the CSV rows
df = pd.DataFrame(csv_rows)

# Display the DataFrame
print(df)
```

### Expected output
The above example will output the following DataFrame:
```
            0            1
0    Header 1    Header 2
1  Row 1, Col 1  Row 1, Col 2
2  Row 2, Col 1  Row 2, Col 2
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

`Feel free to modify this README to better suit your needs.`
