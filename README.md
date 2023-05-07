# Scrapp-and-analyse

This project scrapes and analyzes data from https://www.yad2.co.il/lobby/products.  
First we extract all the information of a certain category, then we download everything and   finally we analyze everything.

# Directory Tree :cactus:
```bash
.
scrap-and-analyse/
│
├── src/ # Source code
│ ├── __init__.py
│ ├── scraper.py # Scraper class
│ ├── utils.py # Utility functions
│ └── settings.py # Project settings
│
├── data/ # Recovered data
│ ├── raw/ # Raw data (unprocessed)
│ └── processed/ # Data processed (cleaned, formatted)
│
├── logs/ # Log files
│
├── testing/ # Unit and integration testing
│ ├── __init__.py
│ └── test_scraper.py
│
├── docs/ # Project documentation
│
├── .gitignore # Files and folders to ignore by Git
├── requirements.txt # List of project dependencies
└── README.md # Project description and instructions

```

## Installation

Create a virtual environment using `python -m venv ./my_venv`.

Activate the virtual environment using `.\my_venv\Scripts\activate` (for Windows)  
or `source ./my_venv/bin/activate` (for Linux/Mac).

Install the required packages using `pip install -r requirements.txt`.


## Usage

run this command: `python ./src/scraper.py`


## Credits

This project uses the following libraries:  

  -`selenium` for the scraping   

