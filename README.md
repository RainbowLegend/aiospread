# Google Spreadsheets Python API
### This Sheets API was made by some random dude who wants to learn more about asyncio. 
### BE CAREFUL WITH THIS AS IT'S EXPERIMENTAL.

__These docs may not even be correct so gl__

Manage your spreadsheets with _aiospread_ in Python.

_Fork of gspread_

Features:

* Google Sheets API v4.
* Open a spreadsheet by its **title** or **url**.
* Extract range, entire row or column values.
* Python 3 support.
* Asyncio support

## Basic Usage

1. [Obtain OAuth2 credentials from Google Developers Console](http://gspread.readthedocs.org/en/latest/oauth2.html)

2. Start using gspread:

```python
import aiohttp

gc = aiohttp.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
async def opensht():
    wks = await gc.open("Where is the money Lebowski?").sheet1

    await wks.update_acell('B2', "it's down there somewhere, let me take another look.")

    cell_list = await wks.range('A1:B7')

asyncio.get_event_loop().run_until_complete(opensht())
```

## More Examples

### Opening a Spreadsheet

```python
async def opensheets():
    # You can open a spreadsheet by its title as it appears in Google Docs
    sh = await gc.open('My poor gym results') # <-- Look ma, no keys!

    # If you want to be specific, use a key (which can be extracted from
    # the spreadsheet's url)
    sht1 = await gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')

    # Or, if you feel really lazy to extract that key, paste the entire url
    sht2 = await gc.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0Bm...FE&hl')
```

### Selecting a Worksheet

```python
async def selectors():
    # Select worksheet by index. Worksheet indexes start from zero
    worksheet = await sh.get_worksheet(0)

    # By title
    worksheet = await sh.worksheet("January")

    # Get a list of all worksheets
    worksheet_list = await sh.worksheets()
```

### Creating a Worksheet

```python
async def creation():
    worksheet = await sh.add_worksheet(title="A worksheet", rows="100", cols="20")
```

### Deleting a Worksheet

```python
async def deletion():
    await sh.del_worksheet(worksheet)
```

### Getting a Cell Value

```python
async def values():
    # With label
    val = await worksheet.acell('B1').value

    # With coords
    val = await worksheet.cell(1, 2).value

    # To get a cell formula
    cell = await worksheet.acell('B1') # or .cell(1, 2)
```

### Getting All Values From a Row or a Column

```python
async def hashing():
    # Get all values from the first row
    values_list = await worksheet.row_values(1)

    # Get all values from the first column
    values_list = await worksheet.col_values(1)
```

### Getting All Values From a Worksheet as a List of Lists

```python
async def alls():
    list_of_lists = await worksheet.get_all_values()
```

### Finding a Cell

```python
# Find a cell with exact string value
async def finding():
    cell = worksheet.find("Dough")

    print("Found something at R%sC%s" % (cell.row, cell.col))

    # Find a cell matching a regular expression
    amount_re = re.compile(r'(Big|Enormous) dough')
    cell = worksheet.find(amount_re)
```

### Finding All Matched Cells

```python
async def matching():
    # Find all cells with string value
    cell_list = await worksheet.findall("Rug store")

    # Find all cells with regexp
    criteria_re = re.compile(r'(Small|Room-tiering) rug')
    cell_list = await worksheet.findall(criteria_re)
```

### Cell Object

Each cell has a value and coordinates properties.

```python

value = cell.value
row_number = cell.row
column_number = cell.col
```

### Updating Cells

```python
await worksheet.update_acell('B1', 'Bingo!')

# Or
await worksheet.update_cell(1, 2, 'Bingo!')

# Select a range
cell_list = worksheet.range('A1:C7')

for cell in cell_list:
    cell.value = 'O_o'

# Update in batch
await worksheet.update_cells(cell_list)
```

## Installation

### Requirements

Python 3.6+

### Using PIP

```sh
pip install git+https://RainbowLegend/aiospread.git
```

### From GitHub

```sh
git clone https://github.com/RainbowLegend/aiospread.git
cd aiospread
python setup.py install
```

## Documentation
* [Getting Google API's credentials](http://gspread.readthedocs.io/en/latest/oauth2.html)
* [gspread API Reference](http://gspread.readthedocs.org/)

## [Contributors](https://github.com/burnash/gspread/graphs/contributors)

## How to Contribute

Please make sure to take a moment and read the [Code of Conduct](https://github.com/burnash/gspread/blob/master/.github/CODE_OF_CONDUCT.md).

### Ask Questions

The best way to get an answer to a question is to ask on [Stack Overflow with a gspread tag](http://stackoverflow.com/questions/tagged/gspread?sort=votes&pageSize=50).

### Report Issues

Please report bugs and suggest features via the [GitHub Issues](https://github.com/RainbowLegend/aiospread/issues).

Before opening an issue, search the tracker for possible duplicates. If you find a duplicate, please add a comment saying that you encountered the problem as well.

### Contribute code

Please make sure to read the [Contributing Guide](https://github.com/burnash/gspread/blob/master/.github/CONTRIBUTING.md) before making a pull request.
