import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_options = Options()
chrome_options.add_argument("--incognito")
serv_obj=Service("C:\Drivers\chromedriver_win32 (1)\chromedriver.exe")

driver=webdriver.Chrome(options=chrome_options,service=serv_obj)
driver.maximize_window()
driver.get("https://this-person-does-not-exist.com/en")

element=driver.find_element(By.NAME,"gender")
drp=Select(element)
drp.select_by_value("male")
time.sleep(2)

element=driver.find_element(By.NAME,"age")
drp=Select(element)
drp.select_by_value("12-18")
time.sleep(2)

element=driver.find_element(By.NAME,"etnic")
drp=Select(element)
drp.select_by_value("asian")
time.sleep(2)

element=driver.find_element(By.ID,"reload-button").click()
time.sleep(15)

driver.execute_script("window.scrollBy(0,400)","")
time.sleep(15)

driver.execute_script("window.scrollBy(0,600)","")
time.sleep(15)

def close_tabs():
    current_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        if handle != current_handle:
            driver.close()
    driver.switch_to.window(current_handle)
def image_download():
    driver.find_element(By.ID,'oldButtonDownload').click()
    driver.switch_to.window((driver.window_handles[1]))
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'download-page-avatar').click()
    time.sleep(35)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://this-person-does-not-exist.com/en")
    time.sleep(5)
    close_tabs()
n=2
for i in range(n):
    image_download()
print("Done")

driver.find_element(By.ID,"oldButtonDownload").click()
time.sleep(15)

driver.find_element(By.ID,"download-button").click()

print(driver.title)
driver.close()
