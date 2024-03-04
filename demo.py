import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

serv_obj = Service("C:\\Program Files\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=option)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@id='name']").send_keys("lukesh")
# driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test12341@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234567890")
# driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("pune")
# driver.find_element(By.ID, "male").click()
#
# # driver.find_element(By.XPATH, "//label[contains(text(),'Sunday')]").click()
#
# days = driver.find_elements(By.XPATH, "//div[@class='form-group']/div/label[contains(text(),'day')]")
# # list1 = ["Sunday", "Monday", "Thursday"]
# idx = 0
# for day in days:
#     # if day.text == list1[idx]:
#     if day.text == "Sunday" or day.text == 'Monday':
#         day.click()
#         # idx += 1
# # using For loop
# # countrys = driver.find_elements(By.XPATH, "//select[@id='country']/option")
# # for country in countrys:
# #     if country.text == "India":
# #         country.click()
#
# # Using select class
# countrys = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
# # countrys.select_by_visible_text("India")
# # countrys.select_by_index(9)
# countrys.select_by_value("germany")
#
# colors = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
# # colors.select_by_visible_text('Green')
# # colors.select_by_index(2)
# colors.select_by_value('white')
#
# # date picker
# yr = '2026'
# mon = 'March'
# date = '20'
# driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
#
# while True:
#     year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#     month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     if mon == month and yr == year:
#         break
#     else:
#         driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # Next button
#         # driver.find_element(By.XPATH, "//span[contains(@class,'ui-icon ui-icon-circle-triangle-w')]").click() # back
#
# dates = driver.find_elements(By.XPATH, "//table[contains(@class,'ui-datepicker-calendar')]/tbody/tr/td")
# for ele in dates:
#     if ele.text == date:
#         ele.click()
#         break
#
# # Web table static
# totalNumerOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
# print(totalNumerOfRows)
#
# for r in range(2, totalNumerOfRows + 1):
#     author = driver.find_element(By.XPATH, "//table[contains(@name,'BookTable')]/tbody/tr[" + str(r) + "]/td[2]").text
#     if author == "Mukesh":
#         BookName = driver.find_element(By.XPATH,
#                                        "//table[contains(@name,'BookTable')]/tbody/tr[" + str(r) + "]/td[1]").text
#         Subject = driver.find_element(By.XPATH,
#                                       "//table[contains(@name,'BookTable')]/tbody/tr[" + str(r) + "]/td[3]").text
#         Price = driver.find_element(By.XPATH,
#                                     "//table[contains(@name,'BookTable')]/tbody/tr[" + str(r) + "]/td[4]").text
#         print(BookName, " ", Subject, " ", Price)
#
# totalNumerOfColumn = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
# for r in range(2, totalNumerOfRows + 1):
#     for c in range(1, totalNumerOfColumn + 1):
#         Data = driver.find_element(By.XPATH,
#                                    "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
#         print(Data, end="   ")
#     print()


# search Box
# driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Selenium")
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# links = driver.find_elements(By.XPATH, "//a[contains(text(),'Selenium')]")

# for link in links:
#     link.click()
# windowID = driver.window_handles
# print(windowID)
#
# for ele in windowID:
#     driver.switch_to.window(ele)
#     print(driver.title)
#

# # Verify text test

# driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Selenium")
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# driver.find_element(By.XPATH, "//a[normalize-space()='Selenium']").click()
# # main page
# print(driver.current_window_handle)
#
# ids = driver.window_handles
# driver.switch_to.window(ids[1])
#
# # child window
# print(driver.current_window_handle)
# expWikipediaText = "From Wikipedia, the free encyclopedia"
# actWikipedialText = driver.find_element(By.CSS_SELECTOR, "#siteSub").text
#
# if actWikipedialText == expWikipediaText:
#     assert True
# else:
#     assert False

# new window
# driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
# time.sleep(10)
# windos = driver.window_handles
# driver.switch_to.window(windos[1])
#
# print(driver.current_window_handle)
# print("child page", driver.title)
# driver.close()
#
# driver.switch_to.window(windos[0])
# print(driver.current_window_handle)
# print("main page title", driver.title)
# driver.close()

# Alert
driver.find_element(By.XPATH, "//button[normalize-space()='Alert']").click()
time.sleep(5)
driver.switch_to.alert.accept()
