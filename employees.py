from selenium import webdriver


def search_by_name(name):
    search = driver.find_element_by_xpath("//input[@name='query']")
    search.send_keys(name)
    button = driver.find_element_by_xpath("//input[@value='Search']")
    button.click()


def delete_by_azonosito(azonosito):
    to_delete = driver.find_element_by_xpath("//tr[td[a[text() = 'azonosito']]]/td[7]/form/input[@value='Delete']".replace("azonosito", azonosito))
    to_delete.click()


def delete_by_name(name):
    to_delete = driver.find_element_by_xpath("//tr[td[contains(., 'name')]]/td[7]/form/input[@value='Delete']".replace("name", name))
    #igy lehet containst hasznalni - td[contains(text(), 'valaki']
    to_delete.click()


def number_of_emps():
    search_by_name("")
    # number_of_emps = driver.find_element_by_xpath("count(//tbody/tr)")
    number_of_emps = len(driver.find_elements_by_xpath("//tbody/tr"))
    return number_of_emps


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
    return monogram


def read_error_message():
    error_message = driver.find_element_by_class_name("invalid-feedback").text
    return error_message


def fill_card_number(card_number):
    card_number_input = driver.find_element_by_id("create-form:card-number-input")
    card_number_input.send_keys(card_number)
    button = driver.find_element_by_id("create-form:save-button")
    button.click()


def full_create(name, card_number):
    create_employee(name)
    driver.implicitly_wait(5)
    fill_card_number(card_number)

def update_employee(oldname,newname):
    update = driver.find_element_by_xpath("//tr[td[contains(., 'name')]]/td[1]/a".replace("name", oldname))
    update.click()
    updateField = driver.find_element_by_xpath("//input[@type = 'text']")
    updateField.clear()
    updateField.send_keys(newname)
    updateButton = updateField = driver.find_element_by_xpath("//input[@type = 'submit']")
    updateButton.click()

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

# create_employee("Teszt Elő")
# fill_card_number("22")

#full_create('Jim Doe', '52')
#update_employee('toUpdate','afterUpdate')



