import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BboSpider(scrapy.Spider):
    name = "bbo"
    allowed_domains = ["bridgebase.com"]
    login_page = "https://ssologin.cuny.edu/cuny.html?resource_url=https%3A%2F%2Fhome.cunyfirst.cuny.edu%252Fpsp%252Fcnyepprd%252FEMPLOYEE%252FEMPL%252Fh%252F%3Ftab%253DDEFAULT"

    def start_requests(login):
        driver = webdriver.PhantomJS()
        driver.get(login)

        driver.find_element_by_id("cf-login").send_keys("perry.raskin18")
        driver.find_element_by_id("password").send_keys("Shmoop11")

        driver.find_element_by_name("submit").click()

        driver.save_screenshot('/Users/perryraskin/Desktop/screen.png')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Student Center")))

        cookies = driver.get_cookies()
        driver.close()

        #yield scrapy.Request("http://www.bridgebase.com/myhands/index.php", cookies=cookies)

    def parse(self, response):
        if "Student Center" in response.body:
            self.log("Login successful")
        else:
            self.log("Login failed")
        print(response.body)

    response = start_requests(login_page)
    parse(response)