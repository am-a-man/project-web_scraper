#type: ignore
import selenium 
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['WDM_LOG_LEVEL'] = '0'
driver = webdriver.Chrome(ChromeDriverManager().install())
search_url='https://careers.microsoft.com/students/us/en/search-results'
driver.get(search_url)


def openOptions(driver):
    try:
        driver.find_element_by_xpath("//button[@aria-label='toggle refine search']").click()
        return True
    except:
        print("check openOptions")
        return True

def dropDown(driver):
    try:
        driver.find_element_by_xpath("//button[@aria-label='Country/Region']").click()
        return True
    except:
        WebDriverWait(driver, timeout = 10).until(openOptions)

def setCountry(driver):
    try:
       
        driver.find_element_by_xpath("//label[input/@data-ph-at-text='India']").click()
      
        return True
    except:
        WebDriverWait(driver, timeout=10).until(dropDown)
        setCountry(driver)


def checkContent(driver):
    

    text = driver.find_elements_by_xpath("//ul[@data-ph-at-id='jobs-list']/li")
    file = open('content.txt', 'w', encoding='utf-8')
   
    for items in text:
  
        header = items.find_element_by_css_selector("h2 a")
       
      
   

        title = header.find_element_by_tag_name('span').text
        link = header.get_attribute('href')

        file.write('=====================\n')
        file.write(title+'\n')
        file.write(link+'\n')

        driver2 = webdriver.Chrome(ChromeDriverManager().install()) 
        driver2.get(link)

        time.sleep(5)

        info = driver2.find_elements_by_xpath("//div[@class='job-description']/div[@class='jd-info']")

        responsibility = info[0]
        qualification = info[1]
        try:
            for i in responsibility.find_element_by_tag_name("h2").text:
                file.write(i)
            file.write('\n\n')
            
            for i in responsibility.find_element_by_tag_name("p").text:
                file.write(i)
            file.write('\n\n')

            for i in qualification.find_element_by_tag_name("h2").text:
                file.write(i)
            file.write('\n\n')

            for i in qualification.find_element_by_tag_name("p").text:
                file.write(i)
            file.write('\n\n')
        except Exception as e:
            print(e)
            return True
        print("writing into file.....")
        driver2.quit()


    file.close()
    return True



def getList(driver):
    try:
        setCountry(driver)
        time.sleep(3)
        checkContent(driver)
        return True
    except KeyboardInterrupt:
        driver.quit()
        exit()
    except:
        getList(driver)


print("wait...")
getList(driver)
driver.quit()
