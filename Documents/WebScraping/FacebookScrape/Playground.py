from selenium import webdriver
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

#options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=/home/bruno/.config/google-chrome/")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'/home/bruno/Downloads/chromedriver_linux64/chromedriver')

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
url = "https://www.facebook.com/alfredocbs10/followers"

driver.get(url)