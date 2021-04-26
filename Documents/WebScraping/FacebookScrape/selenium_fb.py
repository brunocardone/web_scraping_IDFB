import random
from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,random
from selenium.webdriver.common.keys import Keys
import pandas as pd

username = 'bruno.cardone3@gmail.com'
pwd = '!Blmc0507!'

options = Options()
options.headless = False
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=/home/bruno/.config/google-chrome/")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-data-dir=/home/bruno/.config/google-chrome/")
driver = webdriver.Chrome(options=options, executable_path=r'/home/bruno/Downloads/chromedriver_linux64/chromedriver')

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )



#driver.get("https://www.facebook.com/")
#time.sleep(5)
#user_input = driver.find_element_by_xpath("""//*[@id="email"]""")
#pwd_input = driver.find_element_by_xpath("""//*[@id="pass"]""")
#user_input.send_keys(username)
#pwd_input.send_keys(pwd)
#pwd_input.send_keys(Keys.ENTER)
#time.sleep(3)
driver.get("https://www.facebook.com/alfredocbs10/followers")

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    SCROLL_PAUSE_TIME = random.randint(7, 35)
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    print(f"Pausado por {SCROLL_PAUSE_TIME} segundos.")
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    elems = driver.find_elements_by_xpath("//a[@href]")
    lista_urls =[]
    for elem in elems:
        item = elem.get_attribute("href")
        if item in lista_urls:
            pass
        else:
            lista_urls.append(item)
        lista_excel = pd.DataFrame(lista_urls, columns=['FB URL'])
    print(lista_excel.tail(5))
    lista_excel.to_csv('Lista Alfredo.csv', index=False)
    #print(elem.get_attribute("href"))


    if new_height == last_height:
        break
    last_height = new_height



#driver.quit()




#elems = driver.find_elements_by_xpath("//a[@href]")
#for elem in elems:
 #   print(elem.get_attribute("href"))