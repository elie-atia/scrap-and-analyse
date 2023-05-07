from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selectors import CATEGORY_CARD_LIST_XPATH,CARD_PARENT_CSS,PRICE_CSS,TITLE_CSS
import csv


MAX_WAIT_TIME = 50       

class Scrapper:  
    def __init__(self,url,output_file,driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.driver.get(url)
        self.output_file = output_file

    def run(self):
        print("run scraper called")
        time.sleep(8)
        category_links = self.get_category_links()
        properties_data = []

        for link in ['https://www.yad2.co.il/products/furniture?category=2']:
            self.driver.get(link)
            properties_data.extend(self.get_properties_data())

        print(properties_data)

        self.write_properties_to_csv(properties_data)
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


    def write_properties_to_csv(self, properties_data):
        with open(self.output_file, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["description", "price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for property_data in properties_data:
                writer.writerow(property_data)



    def wait_for_clickable_and_click(self,XPATH):
        button = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH,XPATH)))
        button.click()

