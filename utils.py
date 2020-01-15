from selenium import webdriver


def chrome_driver_initiator():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080");
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    driver = webdriver.Chrome('C:/Users/Shankar/Downloads/chromedriver', chrome_options=options)
    return driver