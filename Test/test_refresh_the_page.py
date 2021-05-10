import time


class Test_refresh_the_page:

    def __init__(self, driver):
        self.driver = driver

    def refresh_the_page(self):
        time.sleep(5)
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("273001")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
        self.driver.find_element_by_xpath("//label[contains(text(),'Free')]").click()