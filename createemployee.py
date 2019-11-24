import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def print_welcome():
    print("Kezdődhet a tesztelés")


def click_to_name_input():
    input_field = driver.find_element_by_id('create-form:name-input')
    # input_field = driver.find_element_by_xpath("//input[@type = 'text']")
    input_field.click()


def type_name_input(name):
    input_field = driver.find_element_by_id('create-form:name-input')
    input_field.send_keys(name)


def click_to_header():
    header = driver.find_element_by_xpath("//div//h1")
    header.click()


def wait_for_error_message(message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"),
                                                          message)
    )
    error_message = driver.find_element_by_class_name("invalid-feedback").text
    print(error_message)


def wait_for_monogram(expected_monogram):
     WebDriverWait(driver,10).until(
        expected_conditions.text_to_be_present_in_element((By.ID,"create-form:monogram-text"),  expected_monogram)
     )
     return driver.find_element_by_id("create-form:monogram-text").text


def click_to_create_employee_button():
    driver.find_element_by_id("create-form:save-button").click()


def type_to_card_input_with_random_number(card_number):
    card_number_input = driver.find_element_by_id("create-form:card-number-input")
    card_number_input.send_keys(card_number + str(time.time()))
    #button = driver.find_element_by_id("create-form:save-button")
    #button.click()


chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")




#input_field.click()



#print_welcome()
click_to_name_input()

#click_to_header()
#wait_for_error_message("Az alkalmazott nevét meg kell adni!")

type_name_input("Uj Alkamazott X")
wait_for_monogram("UAX")
click_to_create_employee_button()
type_to_card_input_with_random_number("28645654")
click_to_create_employee_button()


#várakoztatás
#WebDriverWait(driver,10).until(
#    expected_conditions.text_to_be_present_in_element((By.XPATH,"//span[@class = 'invalid-feedback']"), "Az alkalmazott nevét meg kell adni!")
#)
#error_message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
#error_message = driver.find_element_by_class_name("invalid-feedback").text
#print(error_message)



