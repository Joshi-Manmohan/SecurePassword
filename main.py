SECURE = {
    's': '$',
    'and': '&',
    'a': '@',
    'o': '0',
    'm': '%',
    'I': '|',
    'n': '*'
}

def securePassword(password):
    for a, b in SECURE.items():
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password\n")
    password = securePassword(password)
    print(f"Your secure password is {password}")
