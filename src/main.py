import time
from scraper import Scrapper
from settings import EXCUTABLE_PATH, CHROMEDRIVER_PATH, OUTPUT_FILE
import os    

URL = "https://www.yad2.co.il/lobby/products"


def main():  

    start = time.time()
    print(OUTPUT_FILE)
    my_scraper = Scrapper(url=URL,output_file=OUTPUT_FILE,driver_path=CHROMEDRIVER_PATH)
    my_scraper.run()
    stop = time.time()    
    print(f"Time taken by the function:{stop - start} seconds")

if __name__ == '__main__':
    main() 