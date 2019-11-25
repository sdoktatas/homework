import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_cim():
    driver.find_element_by_xpath("//h1").click()


def create_location(name, coords):
    first_create_buton = driver.find_element_by_id("create-location-link")
    first_create_buton.click()
    WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located((By.ID, "location-form"))
    )
    name_input_field = driver.find_element_by_id("location-name")
    name_input_field.send_keys(name)
    coord_input_field = driver.find_element_by_id("location-coords")
    coord_input_field.send_keys(coords)
    second_create_button = driver.find_element(By.XPATH, "//input[@type = 'submit' and @value = 'Create location']")
    second_create_button.click()


def wait_for_location_creation():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"), "Location has created")
    )


def find_created_location_with_wait(name):
    driver.refresh()
    element_xpath = "//tr[td[contains(text(), 'name')]]".replace('name', name)
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, element_xpath))
    )
    #print(element_xpath)


def create_location_test(name, coords):
    name_ts = name + str(time.time())
    #print(name)
    create_location(name_ts, coords)
    #wait_for_location_creation()
    find_created_location_with_wait(name_ts)


def modify_by_name(oldname, newname):
    xpath = "//tr[td[text()='name']]/td[last()]/button[text()='Edit']".replace("name", oldname)
    print(xpath)
    edit_button = driver.find_element_by_xpath(xpath)
    # edit_button.click()


chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)
driver.get(" http://www.learnwebservices.com/locations/?size=100")


# create_location("vadiuj", "47.4979,19.0402")
# wait_for_location_creation()
# find_created_location_with_wait('vadiuj')
# create_location_test("a3", "47.4979,19.0402")

modify_by_name("Almafalva", "Uj")


