import time


class Test_call:

    def __init__(self, driver):
        self.driver = driver

    def call_me(self):
        self.driver.execute_script("window.open('');")

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://dashboard.clicksend.com/")

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("username").send_keys("anoop.gupta@soprasteria.com")
        self.driver.find_element_by_name("password").send_keys("Me@astro024")
        self.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]").click()

        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector("ul.nav.nav-main li:nth-child(7) a.auto.grayhyperlink").click()

        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector("ul.nav.nav-main li:nth-child(7) ul.nav.dk li:nth-child(1)").click()

        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//textarea[@id='searchInput']").send_keys("8826360661")
        self.driver.find_element_by_xpath("//textarea[@id='input_1']").send_keys("slot is available")
        self.driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(5)

        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector("button.btn.btn-success.form-control.sms_sendbtn").click()

    def play_youtube(self):
        self.driver.execute_script("window.open('');")

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.youtube.com/")

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='search']").send_keys("raabta")
        self.driver.find_element_by_xpath("//ytd-masthead/div[@id='container']/div[@id='center']/ytd-searchbox[@id='search']/form[@id='search-form']/button[@id='search-icon-legacy']/yt-icon[1]").click()

        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_css_selector("div.style-scope.ytd-item-section-renderer ytd-video-renderer:nth-child(1)  div.style-scope.ytd-video-renderer div.style-scope.ytd-video-renderer h3.title-and-badge.style-scope.ytd-video-renderer a.yt-simple-endpoint.style-scope.ytd-video-renderer yt-formatted-string.style-scope.ytd-video-renderer").click()

