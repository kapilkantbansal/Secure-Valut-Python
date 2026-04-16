from storage import load_data, save_data, initialize
import getpass
initialize()
print("==============")
print("PASSWORD MANAGER")
print("==============")

def authenticate():
    data=load_data()
    master=data["master_password"]
    if master == "":
        print("WELOCME!No master password is found")
        new_pass=input("Create your master password: ")
        data["master_password"]=new_pass
        save_data(data)

        print("Master password created successfully")
        return True
    else:
        enter_pass=getpass.getpass("Please enter your master password: ")
        if data["master_password"]==enter_pass:
            print("Successfully logged ")
            return True
        else:
            print("ACCESS DENIED")
            return False

def ShowMenu():
    print("1:ADD CREDENTIALS")
    print("2:VIEW ALL CREDENTIALS")
    print("3:SEARCH CREDENTIALS")
    print("4:DELETE CREDENTIAL")
    print("5:EXIT")


def Add():
    print("====ADD CREDENTIALS====")
    data = load_data()
    website = input("Enter website name: ")
    usr = input("USERNAME: ")
    pwd = input("PASSWORD: ")
    data["data"][website] = {
        "username": usr,
        "password": pwd
    }
    save_data(data)


def View():
    print("====VIEW ALL CREDENTIALS====")
    data = load_data()
    vault = data["data"]
    if (vault == 0):
        print("your vault is empty")
    else:
        print("Saved websites are: ")
        for site in vault.keys():
            print(f"{site}")


def Search():
    print("====SEARCH CREDENTIALS====")
    data=load_data()
    query=input("Please enter the site name: ")
    if query in data["data"]:
        info=data["data"][query]
        print(f"Found credential for {query}: ")
        print(f"USERNAME: {info['username' ]}")
        print(f"Password: {info['password']}")
    else:
        print("No such site exist in database")

def Delete():
    print("====DELETE CREDENTIAL====")
    data = load_data()
    site_to_delete=input("Please enter the website name you want to delete: ")
    if site_to_delete in data["data"]:
        del data["data"][site_to_delete]
        save_data(data)
        print(f"{site_to_delete} is successfully deleted")
    else:
        print(f"{site_to_delete} not found in vault")

def Exit():
    print("====EXIT====")
    quit()

if not authenticate():
    exit()
    
while True:
    ShowMenu()
    try:
        input_user = int(input("Enter the choice:"))
        mapping = {
            1: Add,
            2: View,
            3: Search,
            4: Delete,
            5: Exit
        }

        func = mapping[input_user]

        if func:
            func()
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please enter a valid choice")
    except KeyError:
        print("Please enter a valid choice")
