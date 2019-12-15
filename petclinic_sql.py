from mysql.connector import connect

conn = connect(
    host="localhost",
    user="petclinic",
    passwd="petclinic",
    database="petclinic"
)

def print_owner_names():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM owners")
    for (first_name, last_name) in cursor:
        print(f"{first_name} {last_name}")
    cursor.close()

def list_owner_names():
    names = []
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM owners")
    for (first_name, last_name) in cursor:
        names.append(f"{first_name} {last_name}")
    cursor.close()
    return names


def list_owner_names_who_lives_in(city):
    names = []
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM owners WHERE city = %s", (city, ))
    for (first_name, last_name) in cursor:
        names.append(f"{first_name} {last_name}")
    cursor.close()
    return names


def find_owner_by_id(id):

    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name, address, city, telephone FROM owners WHERE id = %s", (id,))
    for (first_name,last_name, address, city, telephone) in cursor:
        owner = {"name": first_name + " " + last_name, "address": address, "city": city, "telephone": telephone}
    return owner


def count_owners_who_lives_in(city):
    cursor = conn.cursor()
    count_found = 0
    cursor.execute("select count(*) from owners where city = %s", (city,))
    for (count,) in cursor:
        count_found = count
    cursor.close()
    return count_found


def create_owner_with(name, address, city, telephone):
    parts = name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    cursor = conn.cursor()
    cursor.execute("insert into owners (first_name,last_name, address,city, telephone) values(%s,%s,%s,%s,%s)",
                   (first_name, last_name, address, city, telephone))
    conn.commit()
    cursor.close()


def create_owner(owner):
    name = owner["name"]
    parts = name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    address = owner["address"]
    city = owner["city"]
    telephone = owner["telephone"]
    cursor = conn.cursor()
    cursor.execute("insert into owners (first_name,last_name, address,city, telephone) values(%s,%s,%s,%s,%s)",
                   (first_name, last_name, address, city, telephone))
    conn.commit()
    cursor.close()


def assert_owner_exists(name):
    parts = name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    cursor = conn.cursor()
    owner_found = 0
    cursor.execute("select count(*) from owners where first_name = %s and last_name= %s", (first_name, last_name))
    for (count,) in cursor:
        owner_found += count
    cursor.close()
    return owner_found > 0


def delete_owner_by_id(id):
    cursor = conn.cursor()
    owner_found = 0
    cursor.execute("delete from owners where id = %s", (id,))
    conn.commit()


def pet_names_younger_than(date):
    names = []
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM pets p WHERE p.birth_date > %s", (date,))
    for (name,) in cursor:
        names.append(name)
    cursor.close()
    return names


def get_owner_of(pet_name):
    cursor = conn.cursor()
    cursor.execute("SELECT OWNER_ID FROM PETS WHERE NAME = %s", (pet_name,))
    for (found_id, ) in cursor:
        owner_id = (found_id)
    cursor.close()
    owner = find_owner_by_id(owner_id)
    return owner["name"]


def add_owner_to(owner_name, pet_name, birth_date, type_name):
    parts = owner_name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    cursor = conn.cursor()
    cursor.execute("select id from owners where first_name = %s and last_name= %s", (first_name, last_name))
    for (ow_id,) in cursor:
        owner_id = ow_id
    cursor.execute("SELECT id from types WHERE NAME = %s", (type_name,))
    for (t_id,) in cursor:
        type_id = t_id
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pets (name,birth_date,type_id,owner_id) VALUES (%s,%s,%s,%s)",(pet_name, birth_date, type_id, owner_id))
    conn.commit()
    cursor.close()


def get_pets_of(owner_name):
    pets = []
    parts = owner_name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    cursor = conn.cursor()
    cursor.execute(
        "SELECT p.NAME,p.birth_date,t.name FROM pets p inner join owners o ON p.owner_id = o.id inner join types t ON p.type_id = t.id where owner_id in (select id from owners WHERE o.first_name =%s AND o.last_name=%s)",
        (first_name, last_name))
    for (name, birth_date, type) in cursor:
        pets.append({"name": name, "birth_date": str(birth_date), "type": type})
    cursor.close()
    return pets


def print_visits_of(pet_name):
    visits = []
    cursor = conn.cursor()
    cursor.execute("SELECT v.visit_date,v.description FROM pets p join visits v ON p.id = v.pet_id WHERE p.name = %s", (pet_name,))
    for (visit_date, description) in cursor:
        visits.append(f"{visit_date} {description}")
    cursor.close()
    print(visits)

# print_owner_names()
# print(list_owner_names())
# print(list_owner_names_who_lives_in('Madison'))
# print(find_owner_by_id("1"))
# print(count_owners_who_lives_in("Madison"))
# create_owner_with("Lajcsi Lagzi", "Trombita utca 24.", "Csalyágaröcsöge", "555")
# print_owner_names()
# owner = {"name": "Boborján Kis", "address": "Vastyúk u. 1..", "city": "Budapest", "telephone": "123456"}
# create_owner(owner)
# print_owner_names()
# print(assert_owner_exists("George Franklin"))
# print(assert_owner_exists("Boborjan Kis"))
# delete_owner_by_id(12)
# print(pet_names_younger_than('2000-01-01'))
# print(get_owner_of("Leo"))
# add_owner_to("Lajcsi Lagzi","Karcsika","2015-06-20","cat")
# print(get_pets_of("Lajcsi Lagzi"))
# print_visits_of("Max")
