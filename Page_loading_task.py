#Start Button xpath: //div[contains(@class,"GamePostStart_btn__yoMra btn") and text()="Start"]

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = r"https://mathup.com/games/crossbit?mode=championship"
driver = webdriver.Chrome(service=Service())

def get_difficulty(url,total_time,iterations=10):
    for _ in range(1,iterations+1):
        try:
            start_time = time.time()
            driver.get(url)

            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,r'//div[contains(@class,"GamePostStart_btn__yoMra btn") and text()="Start"]')))
            total_time += (time.time() - start_time)
            
        except Exception as e:
            print(e)
        
    driver.close()
    avg_time = total_time/iterations
    print(f"Average Time: {avg_time}, Total Time: {total_time}")
    
total_time = 0
get_difficulty(url,total_time)


