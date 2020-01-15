from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from parsel import Selector
import parameters
from time import sleep
import csv

driver = webdriver.Chrome('C:/Users/Shankar/Downloads/chromedriver')

driver.get('https://www.linkedin.com/login?')
# driver.find_element_by_link_text('Sign in')
username = driver.find_element_by_id('username')
username.send_keys(parameters.linkedin_username)
sleep(0.5)
password = driver.find_element_by_id('password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)

log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

log_in_button.click()
sleep(0.5)
driver.get('https://www.google.com/')
sleep(3)
search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)
search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_css_selector('#res a')

writer = csv.writer(open(parameters.file_name, 'w'))

linkedin_urls = [url.get_attribute('href') for url in linkedin_urls]
writer.writerow(['Name', 'Summary', 'Location','Company','College','URL'])
for ln_urls in linkedin_urls:
    listq = []
    check_for_linkedin = ln_urls.split('/')[2]
    if check_for_linkedin == 'in.linkedin.com':
        driver.get(ln_urls)
        sel = Selector(text=driver.page_source)
        name = sel.xpath('//*[@class="inline t-24 t-black t-normal break-words"]/text()').extract_first()
        sleep(1)
        summary = sel.xpath('//*[@class="mt1 t-18 t-black t-normal"]/text()').extract_first()
        sleep(1)
        location = sel.xpath('//*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first()
        sleep(1)
        url = driver.current_url

        company =  sel.xpath('//a[@data-control-name="position_see_more"]/span/text()').extract_first()

        college = sel.xpath('//a[@data-control-name="education_see_more"]/span/text()').extract_first()


        sleep(1)
        if name:
            name = name.strip()

        if summary:
            summary = summary.strip()

        if location:
            location = location.strip()

        if company:
            company = company.strip()

        if college:
            college = college.strip()


        writer.writerow([name,
                         summary,
                         location,
                         company,
                         college,
                         url])
driver.quit()




