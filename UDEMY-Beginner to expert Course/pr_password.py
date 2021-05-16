our_password="pass123"
your_answers=""
no_of_try=7
no_max_of_try=9
max_try="not reached"

while your_answers != our_password and max_try!="Reached":
    if no_max_of_try > no_of_try:
        your_answers =input("enter your password")
        no_of_try = no_of_try + 1
    else:max_try="Reached"


if max_try!="Reached":
    print("Account block")
else:print("Access granted")