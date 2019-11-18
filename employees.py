from selenium import webdriver


def search_by_name(name):
    search = driver.find_element_by_xpath("//input[@name='query']")
    search.send_keys(name)
    button = driver.find_element_by_xpath("//input[@value='Search']")
    button.click()


def delete_by_azonosito(azonosito):
    to_delete = driver.find_element_by_xpath(
        "//tr[td[a[text() = 'azonosito']]]/td[8]/form/input[@value='Delete']".replace("azonosito", azonosito))
    to_delete.click()


def delete_by_name(name):
    to_delete = driver.find_element_by_xpath(
        "//tr[td[contains(., 'name')]]/td[8]/form/input[@value='Delete']".replace("name", name))
    to_delete.click()


def number_of_emps():
    search_by_name("")
    # number_of_emps = driver.find_element_by_xpath("count(//tbody/tr)")
    number_of_emps = len(driver.find_elements_by_xpath("//tbody/tr"))
    return number_of_emps
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

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

# print('Írj egy olyan függényt, mely paraméterként kap egy szót, és az alapján szűri a táblázatot! A felső mezőbe kell beírni, majd megnyomni a Search gombot.')
# search_by_name('John Doe')
# print("Írj egy olyan függvényt, mely a paraméterként kapott azonosítójú alkalmazottat kitörli!")
# delete_by_azonosito('93f8323b-c607-4a25-b263-4a4c90ae554a')
# print("Írj egy olyan függvényt, mely a paraméterként kapott nevű alkalmazottat kitörli!")
# delete_by_name('torlendo')
# print("Írj egy olyan függvényt, mely kiírja, hogy hány alkalmazott van!")
# print(number_of_emps())
# print("Írj egy függvényt, ami magyarra vált, és egy másik függvényt, amely angolra vált!")
# change_to_hun()
# change_to_eng()
# print("Írj egy függvényt, mely kap egy paramétert, ez lesz az alkalmazott neve! Megnyomja a Create employee linket, majd kitölti a beviteli mezőt.")
# create_employee("Kovács Géza")
# print("Írj egy függvényt, mely visszaolvassa a monogramot!")
# driver.implicitly_wait(20)
# print("monogram" + read_monogram())
# print("Írj egy függvényt, ami visszaolvassa a hibaüzenetet! ")
# create_employee("")
# print(read_error_message())
# print("Írj egy függvényt, mely paraméterek alapján beírj a második képernyőn a kártyaszámot!")
create_employee("Teszt Elő")
fill_card_number("22")
# print("Írj egy függvényt, mely kap egy nevet és egy kártyaszámot, és a paraméterekkel meghívja az előző két függvényt")
full_create('Jim Doe', '52')

driver.quit()
