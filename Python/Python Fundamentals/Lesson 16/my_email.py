email = input()
command = ''

while command == "Complete":
    command = input()
    if command == "Make Upper":
        temp = ''
        for i in range(len(email)):
            if email[i].isalpfa():

                temp = temp + email[i].upper()
            else:
                temp = temp + email
        print(temp)

    elif command == "Make Lower":
        temp = ''
        for i in range(len(email)):
            if email[i].isalpfa():

                temp = temp + email[i].lower()
            else:
                temp = temp + email
        print(temp)
    elif command.startswith("GetDomain"):
        count = command.split("-")
        count = count[1] - 1
        temp = email[-count]
        temp = ''
        print(temp)
    elif command.startswith("GetUsername"):
        index = email.find('@')
        if index == -1:
            temp = (f"The email {email} doesn\'t contain the @ symbol")
        else:
            temp = email.split("@")[0]
        print(temp)
    elif command.startswith("Replace"):
        count = command.split()
        temp = email.replace(count[1], "-")
        print(temp)
    elif command.startswith("Encrypt"):
        email = email.encode("ascii")
        temp = " ".join(email)
        print(temp)
