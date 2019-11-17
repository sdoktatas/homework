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

driver = webdriver.Chrome()
driver.get("http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html")

# print(multiplyWithForm(10,5))
# print(multiplyWithForm(2,3))
print(multiplyWithTable(5,6))

# driver.close()
driver.quit()
