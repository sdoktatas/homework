from selenium import webdriver

def search_by_name(name):
    search = driver.find_element_by_xpath("//input[@name='query']")
    search.send_keys(name)
    button = driver.find_element_by_xpath("//input[@value='Search']")
    button.click()

def delete_by_azonosito(azonosito):
    to_delete = driver.find_element_by_xpath("//tr[td[a[text() = 'azonosito']]]/td[8]/form/input[@value='Delete']".replace("azonosito",azonosito))
    to_delete.click()
driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
# search_by_name('John Doe')
delete_by_azonosito('93f8323b-c607-4a25-b263-4a4c90ae554a')
# driver.quit()