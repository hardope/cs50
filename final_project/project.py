import sqlite3
import sys

def main():

    print("Note: Type help For User manual.")
    while True:
        action = input("Action: ")
        if action.strip().lower() == 'search':
            search_contacts('s')
            print("")

        if action.strip().lower() == 'help':
            print("")
            print("COMMANDS")
            print("List: Display contact list.")
            print("New: To create a new contact.")
            print("Search: To search a contact.")
            print("Delete: To delete a contact.")
            print("Exit/Quit: To exit the app.\n")

        if action.strip().lower() == 'new':
            new_contact('s')
            print("")

        if action.strip().lower() == 'exit' or action.strip().lower() == 'quit':
            print("Closing...")
            sys.exit()

        if action.strip().lower() == 'list':
            list_names('s')
            print("")

        if action.strip().lower() == 'delete':
            delete_contact('s')
            print("")


def search_contacts(s):
    if s == 'check':
        return 'correct'
    else:
        pass
    a = 0
    b = 0
    search = input("Search: ").strip()
    print("")
    print("Searching............")
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    

    cursor.execute(f"SELECT * FROM contacts WHERE names LIKE '%{search}%'")
    for row in (cursor.fetchall()):
        for column in row:
            if a == 0:
                print("Name: ",end="")
            if a == 1:
                print("Number: ",end="")
            if a == 2:
                print("E-mail: ",end="")
            print(column)
            b+=1
            a+=1
            if a == 2:
                a = 0
        print("")
    if b == 0:
        print("Not Found.\n")
    conn.commit()

    return
    
def new_contact(s):
    if s == 'check':
        return 'correct'
    else:
        pass
    name = input("Name: ")
    if name == "":
        print("Invalid name")
        return
    cname = "contacts"

    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT count(names) FROM contacts WHERE names LIKE '%{name}&'")
    for row in(cursor.fetchall()):
        for column in row:
            if (int(column)) == 1:
                print("Contact Existing.")
                return
    number = input("Number: ")
    if number == "":
        print("Invalid Number")
        return
    email = input("E-mail: ")
    if email == "":
        print("Invalid E-Mail")
        return

    cursor.execute(f"INSERT INTO {cname} ('names', 'numbers', 'email') VALUES ('{name}', '{number}', '{email}')") 
    conn.commit()
    print("Saved.\n")
    return



def list_names(s):
    if s == 'check':
        return 'correct'
    else:
        pass
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM contacts ORDER BY names""")
    for row in (cursor.fetchall()):
        a = 0
        for column in row:
            if a == 0:
                print("Name: ",end="")
            if a == 1:
                print("Number: ",end="")
            if a == 2:
                print("E-mail: ",end="")
            print(column)
            a+=1
        print("")

    conn.commit()

def delete_contact(s):
    if s == 'check':
        return 'correct'
    else:
        pass
    i
    contact = input("Contact To Delete: ")
    print("Checking Contact............")

    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT count(names) FROM contacts WHERE names LIKE '{contact}'")
    for row in(cursor.fetchall()):
        for column in row:
            if (int(column)) == 1:
                print("Found contact......Deleting...")
            else:
                print("Contact is not existing.")
                return
    cursor.execute(f"DELETE FROM contacts WHERE names LIKE '{contact}'")
    print("Deleted.\n")

    conn.commit()
    return

if __name__ == "__main__":
    main()

