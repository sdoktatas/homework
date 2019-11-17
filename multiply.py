from selenium import webdriver
from selenium.webdriver.common.by import By

def multiplyWithForm(first_number,second_number):
    first_input = driver.find_element_by_id('a-input')
    second_input = driver.find_element_by_id('b-input')
    button = driver.find_element_by_id('calculate-button')
    result = driver.find_element_by_id('result-div')


    first_input.send_keys(first_number)
    second_input.send_keys(second_number)
    button.click()
    first_input.clear()
    second_input.clear()
    return int(result.text)

def multiplyWithTable(first_number,second_number):
    xpath = "//tr[first_number]".replace("first_number",str(first_number)) + "/td[second_number]".replace("second_number",str(second_number))
    # print(xpath)
    result = driver.find_element_by_xpath(xpath)
    return int(result.text)

def multiply(first_number,second_number):
    return int(first_number) * int(second_number)

driver = webdriver.Chrome()
driver.get("http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html")

# print(multiplyWithForm(10,5))
# print(multiplyWithForm(2,3))
# print(multiplyWithTable(5,6))
# print(multiply(2,5))

number_1 = input("Kérem az első számot: ")
number_2 = input("Kérem az második számot: ")

first_result = multiplyWithForm(number_1,number_2)
second_result = multiplyWithTable(number_1,number_2)
third_result = multiply(number_1,number_2)

# print(first_result)
# print(second_result)
# print(third_result)

print(first_result == second_result)
print(second_result == third_result)

# driver.close()
driver.quit()
