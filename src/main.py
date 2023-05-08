import time
from scraper import Scrapper
from settings import EXCUTABLE_PATH, CHROMEDRIVER_PATH, OUTPUT_FILE
import os    

# URL = "https://www.yad2.co.il/lobby/products"
URL_2 = "https://www.yad2.co.il/products/furniture?category=2"

def main():  

    start = time.time()
    my_scraper = Scrapper(url=URL_2,output_file=OUTPUT_FILE,driver_path=CHROMEDRIVER_PATH)
    my_scraper.run()
    stop = time.time()    
    print(f"Time taken by the function:{stop - start} seconds")

if __name__ == '__main__':
    main() 