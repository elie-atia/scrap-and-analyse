import queue
import threading
from selenium.webdriver.common.by import By
from selectors import PRICE_CSS,TITLE_CSS


class ThreadManager:
    
    def __init__(self) -> None:
        self.data_queue = queue.Queue()
        self.consumer_thread = threading.Thread(target=self.consumer, name="Consumer thread")
        self.consumer_thread.start()
        self.data_extracted_by_consumer = []
        self.lock = threading.Lock()
  
    
    def producer(self,data):
        self.data_queue.put(data)
   
    def consumer(self):
        while True:
            try:
                data = self.data_queue.get(block=True, timeout=5)
                if data is None:
                    break
                processed_data = self.process_data(data)
                print(processed_data)
                with self.lock:
                    self.data_extracted_by_consumer.append(processed_data)
            except queue.Empty:
                print("No data in the queue. Waiting for more data.")
            except Exception as e:
                print('error in comsumer',e)
                raise Exception('error in consumer (of threadManager)')
            

    def process_data(self,data):
        return data
    
        
    def save_to_csv(self,filename=""):
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["description", "price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data_extracted_by_consumer:
                writer.writerow(row)


        