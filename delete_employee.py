from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def delete_by_name(name):
    to_delete = driver.find_element_by_xpath("//tr[td[contains(text(), 'name')]]/td[last()]/form/input[2]".replace("name", name))
    #igy lehet containst hasznalni - td[contains(text(), 'valaki']
    to_delete.click()

def find_id_by_name(name):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.Class, "alert alert-info"), "Employee has deleted")
    )
    id = driver.find_element_by_xpath("//tr[td[contains(text(), 'name')]]/td[1]/form/input[@value='Delete']".replace("name", name))






chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")


#find_id_by_name("Uj Alk")
delete_by_name("Uj Alk")