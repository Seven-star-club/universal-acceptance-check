import re
import validators
import socket




def checkDomain(d):
    try:
        return validators.domain.domain(d)

    except Exception as e:
        return False


def good_netloc(netloc):
    try:
        socket.gethostbyname(netloc)
        return True
    except Exception as e:
        return False


print("UNIVERSAL ACCEPTANCE Readiness\n")

listOfMethods = ["Domain Name", "Email syntactical check", "URL syntactical check", "Domain Equivalence check","Exit"]
while True:
    for i in range(5):
        print(str(i + 1) + "." + listOfMethods[i])
    choice = int(input("Enter your choice\n")) - 1
    if choice == 0:
        d_name = input("Enter the domain name to get identified\n")
        decomp_list = d_name.split(".")
        print("DECOMPOSITION\n")
        for i in decomp_list:
            print(i)
        if checkDomain(d_name):
            print("Domain syntax  is valid\n")
        else:
            print("Domain syntax is invalid\n")
        print("TLD:",decomp_list[2])

    elif choice == 1:
        addressToVerify = input("Enter the email to get it checked syntactically\n")
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        if match == None:
            print('Bad Syntax')
            raise ValueError('Bad Syntax')
        else:
            print("Correct syntax")
        decomp_list = addressToVerify.split(".")
        print("DECOMPOSITION")
        for i in decomp_list:
            print(i)

    elif choice == 2:
        url_name = input("Enter the url which need to get identified\n")
        if good_netloc(url_name):
            print("Url is valid")
        else:
            print("Invalid url name")
        decomp_list = url_name.split(".")
        print("DECOMPOSITION")
        for i in decomp_list:
            print(i)

    elif choice == 3:
        one_domain = input("Enter the first domain\n")
        second_domain = input("Enter the second domain\n")
        first = one_domain.split(".")
        second = second_domain.split(".")
        for i in range(3):
            if first[i] != second[i]:
                print("Both are different")
            else:
                print("They are syntactically similar")

    elif choice == 4:
        print("Turning off")
        quit()

    else:
        continue
