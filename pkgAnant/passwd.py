import random
import string
import csv

def exclude_csv(path):
    with open(path, newline='') as csvfile:
        reader=csv.reader(csvfile)
        return set(row[0] for row in reader)

def generate_pass(exclusions):
    len_password = random.randint(6, 12)

    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits

    password=random.choice(lower) + random.choice(upper) + random.choice(num)
    password+=''.join(random.choices(lower + upper + num, k=len_password - 3))
    password=''.join(char for char in password if char not in exclusions)

    password_list=list(password)
    random.shuffle(password_list)
    password=''.join(password_list)
    return password

#calling exclude_csv function to collect all names from names.csv
excluded_names=exclude_csv("names.csv")

#calling exclude_csv function to collect all names from places.csv
excluded_places=exclude_csv("places.csv")

#gathering all names and places which shouldn't be included in password
all_exclusions=excluded_names.union(excluded_places)

def genPass():
    password=generate_pass(all_exclusions)
    return password

#generating password by calling function
# password = genPass()
# print(password)
