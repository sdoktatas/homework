from selenium import webdriver

def search_by_name(name):
    search = driver.find_element_by_xpath("//input[@name='query']")
    search.send_keys(name)
    button = driver.find_element_by_xpath("//input[@value='Search']")
    button.click()

def delete_by_azonosito(azonosito):
    to_delete = driver.find_element_by_xpath("//tr[td[a[text() = 'azonosito']]]/td[8]/form/input[@value='Delete']".replace("azonosito",azonosito))
    to_delete.click()

def delete_by_name(name):
    to_delete = driver.find_element_by_xpath(" // tr[td[contains(., 'name')]]/td[8]/form/input[@value='Delete']".replace("name", name))
    to_delete.click()


def number_of_emps():
    search_by_name("")
    #number_of_emps = driver.find_element_by_xpath("count(//tbody/tr)")
    number_of_emps = len(driver.find_elements_by_xpath("//tbody/tr"))
    return  number_of_emps
    # print(number_of_emps.size)


def change_to_hun():
    magyar = driver.find_element_by_xpath("//a[text()='Magyar']")
    magyar.click()

def change_to_eng():
    angol = driver.find_element_by_xpath("//a[text()='English']")
    angol.click()

def create_employee(name):
    create_button = driver.find_element_by_xpath("//a[text()='Create employee']")
    create_button.click()
    name_input = driver.find_element_by_id('create-form:name-input')
    name_input.send_keys(name)
    driver.find_element_by_id("create-form:save-button").click()

def read_monogram():
    monogram = driver.find_element_by_id("create-form:monogram-text").text
    print("mon" + monogram)
    return monogram

def read_error_message():
    error_message = driver.find_element_by_class_name("invalid-feedback").text
    return error_message



driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

# search_by_name('John Doe')
# delete_by_azonosito('93f8323b-c607-4a25-b263-4a4c90ae554a')
# delete_by_name('torlendo alk')
print(number_of_emps())
#change_to_hun()
#change_to_eng()
#create_employee("Kovács Géza")
#driver.implicitly_wait(20)
#print("monogram" + read_monogram())
#create_employee("")
#print(read_error_message())




#driver.quit()