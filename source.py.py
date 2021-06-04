import os
import selenium
from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(ChromeDriverManager().install())
search_url='https://careers.microsoft.com/students/us/en/search-results'
driver.get(search_url)
os.environ['WDM_LOG_LEVEL'] = '0'


def openOptions(driver):
    try:
        driver.find_element_by_xpath("//button[@aria-label='toggle refine search']").click()
        return True
    except:
        print("check openoptions")
        return True

def dropDown(driver):
    try:
        driver.find_element_by_xpath("//button[@aria-label='Country/Region']").click()
        return True
    except:
        print("error dropDown")
        WebDriverWait(driver, timeout = 10).until(openOptions)

def setCountry(driver):
    try:
       
        driver.find_element_by_xpath("//label[input/@data-ph-at-text='India']").click()
      
        return True
    except:
        print("error setCountry")
        WebDriverWait(driver, timeout=10).until(dropDown)
        setCountry(driver)


def getList(driver):
    try:
        setCountry(driver)
        time.sleep(3)
        text = driver.find_element_by_xpath("//ul[@data-ph-at-id='jobs-list']")
        listItems = text.find_elements_by_tag_name('li')

        for items in listItems:
            print('========================')
            print(type(items.text))
            print(items.text)
            print('========================')
        return True
      
    except:
        print("error checkGetlist")
        getList(driver)

getList(driver)
