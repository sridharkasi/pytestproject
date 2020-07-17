from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_example():
    # driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://www.google.com/")
    print(driver.title)
    driver.close()