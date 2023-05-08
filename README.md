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
│ ├── main.py # File to run the classes of the scraper
│ ├── selectors.py # File to selectors of the scrapers
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
├── drivers/                      # Folder that contains the driver for the browser
│   └── chromedriver.exe          # File chromedriver.exe for Chrome
│ 
├── scripts/ # Scripts and tools
│   ├── connect_vpn.bat
│   └── disconnect_vpn.bat
│
├── .gitignore # Files and folders to ignore by Git
├── requirements.txt # List of project dependencies
├── env.json # File containing the environement variables
├── LICENSE #License of the project
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


## To do

-[ ] Use HTTP requests (with the requests library) instead of Selenium. (Selenium is slower than typical HTTP requests because it launches a browser and executes JavaScript)

-[ ] Use threads to process multiple pages in parallel: create a pool of threads that each process a page and fetch data. Need to ensure that data fetching is thread-safe, i.e. multiple threads can fetch data at the same time without creating concurrency issues.

-[ ] Use a faster data extraction method, like BeautifulSoup which is designed for parsing HTML documents. 

-[ ] Use more specific selectors: Directly find the elements (price and description) instead of using the parent elements. (This can reduce the number of item search operations and speed up data retrieval)

-[ ] Avoid unnecessary waiting times: use timeouts only when absolutely necessary, such as to wait for something to load or to meet a website's request limits.

-[ ] Process the data.

-[ ] Create a view to enable user to download the processed data.
