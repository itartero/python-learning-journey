name = "Nacho"
surname = "Tardajos"

def create_credentials(name, surname):
    username = name[:3].lower() + surname[:4].lower()
    password = ""
    for index in range(len(username)):
        password += username[index - 1]

    return username, password
    

print(create_credentials(name, surname))