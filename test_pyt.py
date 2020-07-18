from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def test_launch():
    global driver
    driver = webdriver.Chrome(executable_path=".\Drivers\chromedriver.exe")
    print(driver.title)
    yield
    driver.close()
def test_launch1(test_launch):
    driver.get("https://www.google.com/")
    print("Page Title: "+driver.title)
    assert driver.title=="google.com"
def test_launch2(test_launch):
    driver.get("https://www.google.com/")
    print("current URl: "+ driver.current_url)
    assert driver.current_url=="https://www.google.com/"