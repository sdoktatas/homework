from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sdoktatas.github.io/homework/triangles.html")
input_a = driver.find_element_by_id("a-input")
input_b = driver.find_element_by_id("b-input")
input_c = driver.find_element_by_id("c-input")
button = driver.find_element_by_id("calculate-button")


input_a.send_keys("3")
input_b.send_keys("3")
input_c.send_keys("3")
button.click()
result = driver.find_element_by_xpath("//li[last()]").text
#print(result)
expected1 = 'a = 3, b = 3, c = 3: Egyenlő oldalú'
assert result == expected1


input_a.clear()
input_b.clear()
input_c.clear()

input_a.send_keys("-1")
input_b.send_keys("3")
input_c.send_keys("3")
button.click()
result = driver.find_element_by_xpath("//li[last()]").text

expected2 = 'a = -1, b = 3, c = 3: Negatív'

assert  result == expected2



