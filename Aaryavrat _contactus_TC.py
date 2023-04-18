from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(executable_path="C:/Users/HomeUser/PycharmProjects/Selenium by sunil/Drivers/chromedriver.exe")
driver.get("https://www.aaryavart.org/")
driver.maximize_window()
driver.find_element("xpath","//input[@placeholder='Full Name']").send_keys("1234")
driver.find_element("xpath","//input[@placeholder='Email']").send_keys("neelam06gmail.com")
driver.find_element("xpath","//input[@placeholder='Contact No.']").send_keys("9901782027")
driver.find_element("xpath","//input[@placeholder='Subject']").send_keys("ASD")
driver.find_element("xpath","//textarea[@placeholder='Your Message']").send_keys("how to find therapist")
driver.find_element("xpath","//input[@type='submit']").click()
sleep(20)

# driver.find_element("xpath","//a[.='wecare@aaryavart.org']").click()
# driver.find_element("xpath","//a[.='Book Appointment']").click()