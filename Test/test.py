from telnetlib import EC
import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_call import Test_call
from test_refresh_the_page import Test_refresh_the_page

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.cowin.gov.in/home")

# driver.find_element_by_class_name("status-switch").click()
driver.implicitly_wait(10)
# driver.find_element_by_class_name("mat-select-arrow-wrapper ng-tns-c64-9").click()
# select = Select(driver.find_element_by_class_name("mat-select-arrow-wrapper ng-tns-c64-9"))
# select.select_by_visible_text("Uttar Pradesh")

driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("273001")
driver.implicitly_wait(10)
# age18to44 = driver.find_element_by_xpath("//label[contains(text(),'Age 18-44')]")
# age18to44.click()
# driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Free')]").click()
time = "infinite"
noofsearch = 0
while(time=="infinite"):
    flag = 0
    for i in range(1, 5):
        forlook = 100
        for j in range(2, 8):
            availability_css = "div.col-padding.matlistingblock div.row:nth-child("+ str(i)+") div.slot-available-main li:nth-child("+str(j)+") div.slots-box div.vaccine-box a"
            agegroupcss = "div.col-padding.matlistingblock div.row:nth-child("+ str(i)+") div.slot-available-main li:nth-child("+str(j)+") div.slots-box div.vaccine-box div span.age-limit"
            try :
                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, availability_css)))
                availability = driver.find_element_by_css_selector(availability_css).text
                agegroup = driver.find_element_by_css_selector(agegroupcss)
                # print(availability, "of" , agegroup.text)
                if availability != "NA":
                    if availability != "Booked":
                        if agegroup.text == "Age 18+":
                            print(agegroup.text)
                            print("no of slot available = ", availability)
                            # Test_call(driver).call_me()
                            Test_call(driver).play_youtube()
                            flag = 1
                            forlook = 101
                            break
            except:
                # print("element not found")
                # flag = 1
                # forlook = 101
                continue
        if forlook == 101:
            break
    i = 0
    j = 0
    noofsearch = noofsearch+1
    print("search completed by times = ", noofsearch)
    print(datetime.datetime.now())
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-padding.matlistingblock div.row:nth-child(1) div.slot-available-main li:nth-child(1) div.slots-box div.vaccine-box a")))
    Test_refresh_the_page(driver).refresh_the_page()
    while(time=="infinite"):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-padding.matlistingblock div.row:nth-child(1) div.slot-available-main li:nth-child(1) div.slots-box div.vaccine-box a")))
            break
        except:
            driver.refresh()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("273001")
            driver.implicitly_wait(10)
            # age18to44 = driver.find_element_by_xpath("//label[contains(text(),'Age 18-44')]")
            # age18to44.click()
            # driver.implicitly_wait(5)
            driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()
            driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
            driver.find_element_by_xpath("//label[contains(text(),'Free')]").click()
            break
    if flag == 1:
        break

print("slot found")

# driver.close()
# driver.quit()