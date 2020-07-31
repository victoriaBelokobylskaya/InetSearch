from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = Options()
chrome_options.add_argument('start-maximized')
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)


driver.get('https://www.mvideo.ru/')


time.sleep(5)

hits = driver.find_elements_by_xpath('.//div[@class="gallery-layout sel-hits-block "]')
hits.pop(0)
hits.pop(1)
hits.pop(1)
goods = []


for hit in hits:
    time.sleep(2) # доделаю позже, что то не получается
    element = driver.find_element_by_xpath("//div[@data-init='ajax-category-carousel']//a[@class='next-btn sel-hits-button-next']")
    # element = hit.find_element_by_css_selector('a.next-btn.sel-hits-button-next')
    hov = ActionChains(driver).move_to_element(element).click()
    hov.perform()

    list = hit.find_elements_by_xpath('.//li[@class="gallery-list-item height-ready"]')
    for li in list:
        hit_d = {}
        hit_d['Product'] = li.find_element_by_class_name('sel-product-tile-title').get_attribute('data-product-info')

        goods.append(hit_d)
        
        


pprint(goods)

