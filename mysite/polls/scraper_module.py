




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class Scrappy:
    def __init__(self, site):
        self.site = site

    def scraping_site(self):
        print('inside method')
        driver = webdriver.Firefox()
        driver.get(self.site)

        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()



















