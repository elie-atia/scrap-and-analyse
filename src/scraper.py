from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selectors import CATEGORY_CARD_LIST_XPATH,CARD_PARENT_CSS,PRICE_CSS,TITLE_CSS,NUM_OF_PAGES_CSS
import csv
import urllib.parse


MAX_WAIT_TIME = 50       

class Scrapper:  
    def __init__(self,url,output_file,driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.url = url
        self.driver.get(url)
        self.output_file = output_file

    def get_num_of_pages(self):
        num_of_pages_element = self.driver.find_element(By.CSS_SELECTOR,NUM_OF_PAGES_CSS)
        return int(num_of_pages_element.text)

    def scrape_all_pages(self):
        num_of_pages = self.get_num_of_pages()
        all_properties_data = []

        for page in range(1, num_of_pages + 1):
            print(f"Scraping page {page} of {num_of_pages}")
            properties_data = self.get_properties_data()
            all_properties_data.extend(properties_data)
            self.go_to_page(page)

        return all_properties_data

    def go_to_page(self,page):
        url_parts = list(urllib.parse.urlparse(self.url))
        query = dict(urllib.parse.parse_qsl(url_parts[4]))
        query["page"] = str(page)
        url_parts[4] = urllib.parse.urlencode(query)
        next_page_url = urllib.parse.urlunparse(url_parts)

        self.driver.get(next_page_url)


    def run(self):
        print("run scraper called")
        time.sleep(8)
        all_properties_data = self.scrape_all_pages()
        
        self.save_to_csv(all_properties_data)
        self.driver.quit()        

    def get_category_links(self):
        # Récupérer les liens des catégories en utilisant leurs sélecteurs CSS ou XPath
        print('get_category_links')
        links = []
        category_card_list = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.element_to_be_clickable((By.XPATH, CATEGORY_CARD_LIST_XPATH)))
        category_card_links = category_card_list.find_elements(By.TAG_NAME,'a')
        links = [link.get_attribute('href') for link in category_card_links]

        return links


    def get_properties_data(self):
        # Récupérer les éléments parents en utilisant leur sélecteur
        parent_elements = self.driver.find_elements(By.CSS_SELECTOR,CARD_PARENT_CSS)

        # Extraire les données des éléments
        properties_data = []
        for parent in parent_elements:
            price_element = parent.find_element(By.CSS_SELECTOR ,PRICE_CSS)
            description_element =  parent.find_element(By.CSS_SELECTOR,TITLE_CSS)

            price = price_element.text
            description = description_element.text

            property_data = {"price": price, "description": description}
            properties_data.append(property_data)

        return properties_data


    def save_to_csv(self, data):
        with open(self.output_file, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["description", "price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)



    def wait_for_clickable_and_click(self,XPATH):
        button = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH,XPATH)))
        button.click()

