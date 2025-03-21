#Start Button xpath: //div[contains(@class,"GamePostStart_btn__yoMra btn") and text()="Start"]
#Difficulty Button xpath: //div[text()="Difficulty"]/following-sibling::div[1]

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = r"https://mathup.com/games/crossbit?mode=championship"
driver = webdriver.Chrome(service=Service())
driver.implicitly_wait(10)

def get_difficulty(url,iterations=10):
    for iteration in range(1,iterations+1):
        try:
            driver.get(url)

            driver.find_element(By.XPATH,r'//div[contains(@class,"GamePostStart_btn__yoMra btn") and text()="Start"]').click()
            difficulty = driver.find_element(By.XPATH,r'//div[text()="Difficulty"]/following-sibling::div[1]').text

            print(f"Iteration {iteration}: {difficulty}")
            
        except Exception as e:
            print(e)
            
        time.sleep(2)
        
    driver.close()
    
get_difficulty(url)

