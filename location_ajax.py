import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_cim():
    driver.find_element_by_xpath("//h1").click()


def create_location(name, coords):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//tr[1]/td[1]"))
    )
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


def find_location_with_wait(name):
    # driver.refresh()
    element_xpath = "//tr[td[contains(text(), 'name')]]".replace('name', name)
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, element_xpath))
    )


def modify_by_name(oldname, name):
    newname = name + str(time.time())
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//tr[1]/td[1]"))
    )
    xpath = "//tr[td[text()='name']]/td[last()]/button[text()='Edit']".replace("name", oldname)
    edit_button = driver.find_element_by_xpath(xpath)
    edit_button.click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.ID, "update-location-name"))
    )
    new_name_inmput_field = driver.find_element_by_id("update-location-name")
    new_name_inmput_field.clear()
    new_name_inmput_field.send_keys(newname)
    update_button = driver.find_element(By.XPATH, "//input[@type = 'submit' and @value = 'Update location']")
    update_button.click()
    return newname


def wait_for_location_modification():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"), "Location has modified")
    )


def wait_for_message_display(message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"), message)
    )


def create_location_test(name, coords):
    name_ts = name + str(time.time())
    #print(name)
    create_location(name_ts, coords)
    #wait_for_location_creation()
    find_location_with_wait(name_ts)


def test_modification(original_name, coords, changed_name):
    create_location(original_name, coords)

    find_location_with_wait(original_name)
    new_name = modify_by_name(original_name, changed_name)

    wait_for_location_modification()

    find_location_with_wait(new_name)


def test_alert_message():
    create_location("", "1,1")
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"), "must not be blank;")
    )

def delete_by_id(id):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//tr[1]/td[1]"))
    )
    xpath = "//tr[td[text()='id']]/td[last()]/button[text()='Delete']".replace("id", str(id))
    delete_button = driver.find_element_by_xpath(xpath)
    delete_button.click()
    driver.switch_to_alert().accept()


def wait_for_delete(id):
    xpath = "//tr[td[contains(text(),'id')]]".replace("id", str(id))
    WebDriverWait(driver, 10).until_not(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)
driver.get(" http://www.learnwebservices.com/locations/?size=100")


# create_location("b35", "47.4979,19.0402")
# wait_for_location_creation()
# find_location_with_wait('b35')
# create_location_test("a3", "47.4979,19.0402")

# modify_by_name("a2", "a2_m")
# test_modification("b24", "2,2", "b24M")

# test_alert_message()
delete_by_id('11699')
wait_for_delete('11699')
