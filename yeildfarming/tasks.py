from .models import YeildContract
from celery import Celery

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element, presence_of_element_located
import time

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

app = Celery()


@app.task
def get_pancakeswap_farm_data():
    url = 'https://pancakeswap.finance/farms'

    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--window-size=1920,1080")


    # webdriver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=chrome_options)
    my_webdriver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # for brave browser
    #chrome_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    #chrome_driver_path = "C:\\Users\\dozie\\Downloads\\chromedriver_win32\\chromedriver.exe"
    #webdriver = webdriver.Chrome(chrome_driver_path, options=chrome_options)


    with my_webdriver as driver:
        wait = WebDriverWait(driver, 20)

        driver.get(url)

        wait.until(text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr[12]/td[3]/div/div/div[2]/div/div'), "%"))
        # time.sleep(10)
        # print(driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr[12]/td[3]/div/div/div[2]/div/div'))

        farm_cards = driver.find_elements_by_class_name('sc-bcuVfI')
        # farm_cards = WebDriverWait(driver, 20).until(text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr[12]/td[3]/div/div/div[2]/div/div'), "%"))
        for card in farm_cards[:4]:
            YeildContract.objects.get_or_create(
                yeildpair=card.find_element_by_class_name('jDnmwq').text,
                defaults={
                    'APR':float(card.find_element_by_class_name('dalabt').text.replace('%', '')),
                    'liquidity':int(card.find_element_by_class_name('MlLjM').text.replace('$', '').replace(',', ''))
                }
            )
            
        driver.close()
